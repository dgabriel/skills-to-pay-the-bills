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


def main():
    cases = json.loads((ROOT / 'evaluations/cases.json').read_text())
    results = ROOT / 'evaluations/results'
    for version in ['v1', 'v2', 'current-existing', 'fresh']:
        score_routing(results, version)
    freeze = json.loads((ROOT / 'evaluations/final-descriptions.json').read_text())
    for name, expected in freeze['entry_sha256'].items():
        entry = ROOT / 'skills' / name / 'SKILL.md'
        assert hashlib.sha256(entry.read_bytes()).hexdigest() == expected, 'Entry changed after case authorship'
    for row in json.loads((ROOT / 'evaluations/fresh-cases.json').read_text()):
        assert isinstance(row['expected'], bool)
    current = json.loads((results / 'routing-input-current-existing.json').read_text())
    previous = json.loads((results / 'routing-input-v2.json').read_text())
    assert current['requests'] == previous['requests'], 'Existing 35 requests changed'
    print('Integrity: final entries frozen; existing 35 requests unchanged')
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
    print('PASS: evidence replay complete; intentional fixture failures are expected')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
