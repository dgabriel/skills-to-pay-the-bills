#!/usr/bin/env python3
"""Replay saved evidence locally; report routing scores without changing cases."""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import os
import re
import runpy
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def replay_canonical(root):
    folder = root / 'evaluations/routing-regression'
    if not folder.is_dir():
        return False
    manifest = json.loads((folder / 'manifest.json').read_text())
    for relative, expected in manifest['artifact_sha256'].items():
        assert hashlib.sha256((folder / relative).read_bytes()).hexdigest() == expected, 'Canonical artifact changed: ' + relative
    freeze_path = folder / 'descriptions.json'
    assert hashlib.sha256(freeze_path.read_bytes()).hexdigest() == manifest['descriptions_sha256'], 'Canonical description snapshot changed'
    freeze = json.loads(freeze_path.read_text())
    descriptions = {row['name']: row['description'] for row in freeze['skills']}
    entries = {p.parent.name: p for p in (root / 'skills').glob('*/SKILL.md')}
    assert len(descriptions) == len(freeze['skills'])
    assert set(entries) == set(descriptions) == set(freeze['entry_sha256']), 'Canonical skill set changed; regenerate with a fresh evaluator'
    for name, entry in entries.items():
        text = entry.read_text()
        description = next(line.removeprefix('description: ') for line in text.splitlines()
                           if line.startswith('description: '))
        assert description == descriptions[name], 'Current description changed; rerun the full canonical suite'
        assert hashlib.sha256(entry.read_bytes()).hexdigest() == freeze['entry_sha256'][name], 'Current entry changed after canonical freeze'
    inputs = json.loads((folder / 'routing-input.json').read_text())
    cases = json.loads((folder / 'cases.json').read_text())
    answers = json.loads((folder / 'routing-answers.json').read_text())
    output = json.loads((folder / 'routing-output.json').read_text())
    source_map = json.loads((folder / 'source-map.json').read_text())
    assert inputs['skills'] == freeze['skills']
    assert inputs['requests'] == [{'id': row['id'], 'prompt': row['prompt']} for row in cases]
    ids = {row['id'] for row in cases}
    assert len(ids) == len(cases) == len(output) == len(answers) == manifest['cases']
    assert ids == set(answers) == {row['id'] for row in output}
    assert len({row['id'] for row in output}) == len(output)
    assert all(len(set(row['selected'])) == len(row['selected']) and
               set(row['selected']) <= set(descriptions) for row in output)
    source_data = {}
    for source, copy in source_map['source_files'].items():
        snapshot = folder / copy
        assert snapshot.read_bytes() == (root / source).read_bytes(), 'Historical source differs from canonical copy'
        source_data[source] = json.loads(snapshot.read_text())
    seen = set()
    unique_cases = set()
    for row in cases:
        assert isinstance(row['expected'], bool) and row['target'] in descriptions
        assert answers[row['id']] == {'skill': row['target'], 'expected': row['expected']}
        identity = (row['prompt'], row['target'], row['expected'])
        assert identity not in unique_cases, 'Duplicate canonical target case'
        unique_cases.add(identity)
        digest = hashlib.sha256(json.dumps(identity, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()[:16]
        assert row['id'] == 'r-' + digest, 'Unstable canonical ID'
        assert row['sources'], 'Canonical case has no retained source'
        for source in row['sources']:
            original = {r['id']: r['prompt'] for r in source_data[source['input']]['requests']}
            assert original[source['id']] == row['prompt'], 'Retained request text changed'
            assert source_data[source['answers']][source['id']] == answers[row['id']], 'Retained target label changed'
            key = (source['input'], source['answers'], source['id'])
            assert key not in seen, 'Repeated source occurrence'
            seen.add(key)
    expected_sources = {(source['input'], source['answers'], request['id'])
                        for source in manifest['source_sets']
                        for request in source_data[source['input']]['requests']}
    assert seen == expected_sources, 'Retained routing source omitted'
    assert len(seen) == source_map['retained_occurrences'] == manifest['retained_occurrences']
    correct = sum((answers[row['id']]['skill'] in row['selected']) == answers[row['id']]['expected']
                  for row in output)
    assert correct == manifest['correct'], 'Canonical recorded score changed'
    print(f'Canonical current-description routing: {correct}/{len(output)} target decisions ({len(descriptions)} skills)')
    print(f'Canonical integrity: {len(seen)} retained occurrences, {len(cases)} unique cases; unchanged labels and requests')
    print('Canonical scope: one retained-case evaluator run, not fresh case authorship, quality grading, or native discovery')
    return True


def replay_supplemental(root):
    # Supplemental reports are evidence to retain, never code to import or execute.
    for manifest_path in sorted((root / 'evaluations').glob('*/supplemental-manifest.json')):
        folder = manifest_path.parent
        manifest = json.loads(manifest_path.read_text())
        for relative, expected in manifest['artifact_sha256'].items():
            artifact = folder / relative
            assert artifact.resolve().is_relative_to(folder.resolve()), 'Supplemental artifact escapes evidence folder'
            assert hashlib.sha256(artifact.read_bytes()).hexdigest() == expected, 'Supplemental evidence changed: ' + relative
        print(manifest['label'] + ': retained hashes verified; no fixture code or agent response executed')


def score_routing(results, version):
    inputs = json.loads((results / f'routing-input-{version}.json').read_text())
    answers = json.loads((results / f'routing-answers-{version}.json').read_text())
    output = json.loads((results / f'routing-output-{version}.json').read_text())
    ids = [row['id'] for row in output]
    assert len(ids) == len(set(ids)) == len(answers), 'Missing or duplicate routing output'
    assert set(ids) == {row['id'] for row in inputs['requests']} == set(answers)
    names = {row['name'] for row in inputs['skills']}
    assert all(set(row['selected']) <= names for row in output)
    correct = sum((answers[row['id']]['skill'] in row['selected']) ==
                  answers[row['id']]['expected'] for row in output)
    print(f'Routing {version}: {correct}/{len(answers)} target decisions')
    # A replay verifies recorded evidence; a mismatch is reported, never hidden
    # by changing a prompt, answer, description, or treating it as a run error.


def replay_suite(fixtures, evidence, label, temp):
    work = temp / label
    work.mkdir()
    for name, content in fixtures.items():
        (work / name).write_text(content)
    source = evidence / 'test_booking.py'
    (work / source.name).write_bytes(source.read_bytes())
    run = subprocess.run([sys.executable, '-m', 'unittest', '-v', source.name],
                         cwd=work, capture_output=True, text=True)
    combined = run.stdout + run.stderr
    assert run.returncode == 1, f'{label}: expected known fixture defect to fail'
    assert 'AssertionError' in combined, combined
    assert '\nERROR:' not in combined, 'Collection/environment error, not intended defect'
    match = re.search(r'Ran (\d+) tests?', combined)
    assert match
    print(f'{label}: {match.group(1)} test methods executed; expected adjacency failure, exit 1')


def replay_followup(root):
    folder = root / 'evaluations/follow-up-skills'
    if not folder.is_dir():
        return
    freeze = json.loads((folder / 'final-descriptions.json').read_text())
    descriptions = {row['name']: row['description'] for row in freeze['skills']}
    for name, expected in freeze['entry_sha256'].items():
        entry = root / 'skills' / name / 'SKILL.md'
        if not (root / 'evaluations/routing-regression').is_dir():
            assert hashlib.sha256(entry.read_bytes()).hexdigest() == expected, 'Follow-up entry changed after freeze'
    for name, expected in descriptions.items():
        text = (root / 'skills' / name / 'SKILL.md').read_text()
        actual = next(line.removeprefix('description: ') for line in text.splitlines()
                      if line.startswith('description: '))
        if not (root / 'evaluations/routing-regression').is_dir():
            assert actual == expected, 'Follow-up evaluator description changed'
    authored = json.loads((folder / 'fresh-cases.json').read_text())
    mapping = json.loads((folder / 'case-id-map.json').read_text())
    inputs = json.loads((folder / 'routing-input.json').read_text())
    original = json.loads((folder / 'routing-input-authored-ids.json').read_text())
    answers = json.loads((folder / 'routing-answers.json').read_text())
    output = json.loads((folder / 'routing-output.json').read_text())
    assert inputs['skills'] == original['skills'] == freeze['skills']
    assert set(mapping) == {row['id'] for row in authored}
    assert len(set(mapping.values())) == len(mapping)
    assert inputs['requests'] == [{'id': mapping[row['id']], 'prompt': row['prompt']}
                                  for row in original['requests']], 'Only evaluator IDs may be normalized'
    requests = {row['id']: row['prompt'] for row in inputs['requests']}
    assert len(requests) == len(output) == len(answers) == len(authored)
    assert set(requests) == set(answers) == {row['id'] for row in output}
    assert len({row['id'] for row in output}) == len(output)
    for row in authored:
        assert isinstance(row['expected'], bool)
        assert requests[mapping[row['id']]] == row['prompt'], 'Follow-up authored request changed'
        assert answers[mapping[row['id']]] == {'skill': row['target'], 'expected': row['expected']}
    for name in freeze['entry_sha256']:
        for expected in [True, False]:
            assert sum(row['target'] == name and row['expected'] is expected for row in authored) == 2
    assert all(set(row['selected']) <= set(descriptions) for row in output)
    correct = sum((answers[row['id']]['skill'] in row['selected']) == answers[row['id']]['expected']
                  for row in output)
    print(f'Follow-up fresh opaque-ID routing: {correct}/{len(output)} target decisions')
    initial = json.loads((folder / 'routing-output-authored-ids.json').read_text())
    original_answers = {row['id']: row for row in authored}
    assert len(initial) == len(authored) == len({row['id'] for row in initial})
    assert {row['id'] for row in initial} == set(original_answers)
    assert all(set(row['selected']) <= set(descriptions) for row in initial)
    initial_correct = sum((original_answers[row['id']]['target'] in row['selected']) ==
                          original_answers[row['id']]['expected'] for row in initial)
    print(f'Follow-up initial descriptive-ID routing: {initial_correct}/{len(initial)} (separate, potentially cued)')
    manifest = json.loads((folder / 'manifest.json').read_text())
    for relative, expected in manifest['artifact_sha256'].items():
        assert hashlib.sha256((folder / relative).read_bytes()).hexdigest() == expected, 'Follow-up artifact changed'
    print('Follow-up integrity: frozen entries, unchanged requests, ID-only normalization, 2 positive/2 negative per skill')
    print('Follow-up scope: saved selection evidence only; no behavioral comparison, rollback, legal approval, or bootstrap execution')


def replay_history(root):
    folder = root / 'evaluations/history-skills'
    manifest = json.loads((folder / 'manifest.json').read_text())
    freeze = json.loads((folder / 'final-descriptions.json').read_text())
    descriptions = {row['name']: row['description'] for row in freeze['skills']}
    for name, expected in freeze['entry_sha256'].items():
        entry = root / 'skills' / name / 'SKILL.md'
        if not (root / 'evaluations/routing-regression').is_dir():
            assert hashlib.sha256(entry.read_bytes()).hexdigest() == expected, 'Entry changed after freeze'
        actual = next(line.removeprefix('description: ') for line in entry.read_text().splitlines()
                      if line.startswith('description: '))
        if not (root / 'evaluations/routing-regression').is_dir():
            assert actual == descriptions[name]
    inputs = json.loads((folder / 'routing-input.json').read_text())
    answers = json.loads((folder / 'routing-answers.json').read_text())
    output = json.loads((folder / 'routing-output.json').read_text())
    authored = json.loads((folder / 'fresh-cases.json').read_text())
    assert inputs['skills'] == freeze['skills'], 'Evaluator descriptions differ from freeze'
    authored_map = {row['id']: row for row in authored}
    requests = {row['id']: row['prompt'] for row in inputs['requests']}
    assert len(requests) == len(answers) == len(output) == len(authored_map) == manifest['routing_cases']
    assert len({row['id'] for row in output}) == len(output)
    assert set(requests) == set(answers) == set(authored_map) == {row['id'] for row in output}
    valid_names = set(descriptions)
    for row in authored:
        assert requests[row['id']] == row['prompt'], 'Authored prompt changed for evaluator'
        assert answers[row['id']] == {'skill': row['target'], 'expected': row['expected']}
    for name in freeze['entry_sha256']:
        for expected in [True, False]:
            assert sum(row['target'] == name and row['expected'] is expected for row in authored) == 2
    assert all(set(row['selected']) <= valid_names for row in output)
    correct = sum((answers[row['id']]['skill'] in row['selected']) == answers[row['id']]['expected']
                  for row in output)
    print(f'History skills fresh routing: {correct}/{len(output)} target decisions')
    print('History integrity: four frozen entries, unchanged authored prompts, 2 positive/2 negative per skill')
    for relative, expected in manifest['artifact_sha256'].items():
        assert hashlib.sha256((folder / relative).read_bytes()).hexdigest() == expected, 'Artifact changed'
    for mode in ['baseline', 'with-skill']:
        prose = (folder / 'results' / mode / 'prose-edit/output.md').read_text()
        normalized = ' '.join(prose.lower().split())
        for fact in ['borrowbox', 'monday', '30', 'one building', 'no payments', 'invite-only',
                     'list a tool', 'request dates', 'record its return']:
            assert fact in normalized, f'{mode}: missing fixture fact {fact}'
        assert chr(0x2014) not in prose, f'{mode}: em dash in edit'
        triage = (folder / 'results' / mode / 'review-findings-triage/output.md').read_text()
        assert all(identity in triage for identity in ['F-1', 'F-2', 'F-3', 'F-4'])
        assert 'unverified' in triage.lower(), 'Plan-only output claims unsupported gate state'
        print(f'History paired {mode}: four findings retained; prose facts retained, {len(prose.split())} words, no em dashes')
    for path in (root / 'skills/prose-edit').rglob('*'):
        if path.is_file():
            assert chr(0x2014) not in path.read_text(), 'Em dash in prose package'
    print('History replay: static-output integrity checks only; no agents, review tools, dashboards, or device tests executed')
    replay_followup(root)


def main():
    canonical_current = replay_canonical(ROOT)
    cases = json.loads((ROOT / 'evaluations/cases.json').read_text())
    results = ROOT / 'evaluations/results'
    for version in ['v1', 'v2', 'current-existing', 'fresh']:
        score_routing(results, version)
    freeze = json.loads((ROOT / 'evaluations/final-descriptions.json').read_text())
    editorial_path = ROOT / 'evaluations/editorial-updates.json'
    editorial = json.loads(editorial_path.read_text())['updates'] if editorial_path.is_file() else {}
    assert set(editorial) <= set(freeze['entry_sha256']), 'Unknown editorial entry'
    descriptions = {row['name']: row['description'] for row in freeze['skills']}
    for name, evaluated in freeze['entry_sha256'].items():
        entry = ROOT / 'skills' / name / 'SKILL.md'
        description = next(line.removeprefix('description: ') for line in entry.read_text().splitlines()
                           if line.startswith('description: '))
        if not canonical_current:
            assert description == descriptions[name], 'Description changed after case authorship'
        expected = evaluated
        if name in editorial:
            assert editorial[name]['evaluated_sha256'] == evaluated, 'Original freeze mismatch'
            expected = editorial[name]['current_sha256']
        if not canonical_current:
            assert hashlib.sha256(entry.read_bytes()).hexdigest() == expected, 'Unrecorded entry change'
    for row in json.loads((ROOT / 'evaluations/fresh-cases.json').read_text()):
        assert isinstance(row['expected'], bool)
    current = json.loads((results / 'routing-input-current-existing.json').read_text())
    previous = json.loads((results / 'routing-input-v2.json').read_text())
    assert current['requests'] == previous['requests'], 'Existing 35 requests changed'
    print('Integrity: historical freezes/editorial records retained; current entries checked against canonical snapshot'
          if canonical_current else 'Integrity: original freeze preserved; editorial fingerprints and unchanged descriptions verified')
    print('Integrity: existing 35 requests unchanged')
    fixtures = cases['tasks']['regression-testing']['artifacts']
    with tempfile.TemporaryDirectory(prefix='skill-replay-') as location:
        temp = Path(location)
        for mode in ['baseline', 'with-skill']:
            replay_suite(fixtures, results / mode / 'regression-testing', f'historical-{mode}', temp)
            replay_suite(fixtures, results / 'current-pair' / mode / 'regression-testing', f'current-{mode}', temp)
        design = results / 'with-skill/design-system-workshop/calculate_contrast.py'
        run = subprocess.run([sys.executable, str(design)], cwd=temp, capture_output=True, text=True)
        assert run.returncode == 0, run.stderr
        assert (temp / 'contrast-results.md').read_text() == (design.parent / 'contrast-results.md').read_text()
        previous_cwd = Path.cwd()
        try:
            os.chdir(temp)
            with contextlib.redirect_stdout(io.StringIO()):
                calculator = runpy.run_path(str(design))
        finally:
            os.chdir(previous_cwd)
        for foreground, background in calculator['pairs']:
            minimum = 3 if foreground in ('border', 'focus') else 4.5
            assert calculator['ratio'](foreground, background) >= minimum
        calculator['tokens'].update({'black': '#000000', 'white': '#FFFFFF'})
        assert calculator['ratio']('black', 'white') == 21
        assert calculator['ratio']('white', 'white') == 1
        print('Contrast: 13 unrounded thresholds and 21:1 / 1:1 sanity checks pass')
        verify = results / 'current-pair/with-skill/spec-review/verify_review.py'
        review_work = temp / 'review'
        review_work.mkdir()
        for name, content in cases['tasks']['spec-review']['artifacts'].items():
            (review_work / name).write_text(content)
        (review_work / verify.name).write_bytes(verify.read_bytes())
        run = subprocess.run([sys.executable, verify.name], cwd=review_work, capture_output=True, text=True)
        assert run.returncode == 1 and 'AssertionError' in run.stderr, run.stdout + run.stderr
        print('Current review reproduction: expected unauthorized-state assertion failure, exit 1')
    if (ROOT / 'evaluations/history-skills/manifest.json').is_file():
        replay_history(ROOT)
    replay_supplemental(ROOT)
    print('PASS: evidence replay complete; intentional fixture failures are expected')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
