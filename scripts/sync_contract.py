#!/usr/bin/env python3
"""Maintain standalone contract copies from a single canonical source."""
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check copies without writing')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    canonical = (root / 'shared/execution-contract.md').read_bytes()
    failures = []
    for skill in sorted((root / 'skills').iterdir()):
        if not (skill / 'SKILL.md').is_file():
            continue
        copy = skill / 'references/execution-contract.md'
        if args.check:
            if not copy.is_file() or copy.read_bytes() != canonical:
                failures.append(skill.name)
        else:
            copy.parent.mkdir(exist_ok=True)
            copy.write_bytes(canonical)
    if failures:
        parser.exit(1, 'Contract differs: ' + ', '.join(failures) + '\n')
    print('Contract copies are current.' if args.check else 'Contract copies synchronized.')


if __name__ == '__main__':
    main()
