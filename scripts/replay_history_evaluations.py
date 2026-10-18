#!/usr/bin/env python3
"""Verify history-derived skill evidence without rerunning agents or live tools."""
from pathlib import Path
import hashlib
import json


def replay_followup(root):
    folder = root / 'evaluations/follow-up-skills'
    if not folder.is_dir():
        return
    freeze = json.loads((folder / 'final-descriptions.json').read_text())
    descriptions = {row['name']: row['description'] for row in freeze['skills']}
    for name, expected in freeze['entry_sha256'].items():
        entry = root / 'skills' / name / 'SKILL.md'
        assert hashlib.sha256(entry.read_bytes()).hexdigest() == expected, 'Follow-up entry changed after freeze'
    for name, expected in descriptions.items():
        text = (root / 'skills' / name / 'SKILL.md').read_text()
        actual = next(line.removeprefix('description: ') for line in text.splitlines()
                      if line.startswith('description: '))
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


def replay(root):
    folder = root / 'evaluations/history-skills'
    manifest = json.loads((folder / 'manifest.json').read_text())
    freeze = json.loads((folder / 'final-descriptions.json').read_text())
    descriptions = {row['name']: row['description'] for row in freeze['skills']}
    for name, expected in freeze['entry_sha256'].items():
        entry = root / 'skills' / name / 'SKILL.md'
        assert hashlib.sha256(entry.read_bytes()).hexdigest() == expected, 'Entry changed after freeze'
        actual = next(line.removeprefix('description: ') for line in entry.read_text().splitlines()
                      if line.startswith('description: '))
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


if __name__ == '__main__':
    replay(Path(__file__).resolve().parents[1])
