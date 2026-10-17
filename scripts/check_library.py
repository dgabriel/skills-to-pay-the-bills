#!/usr/bin/env python3
"""Check portable packages, references, metadata, and basic privacy hygiene."""
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    errors = []
    links = 0
    rename_notes = root / 'RENAMES.md'
    old_names = re.findall(r'renamed from `([^`]+)`', rename_notes.read_text()) if rename_notes.is_file() else []
    canonical = (root / 'shared/execution-contract.md').read_bytes()
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    for entry in skills:
        text = entry.read_text()
        skill = entry.parent
        # Full YAML validation is also run with the host skill validator.
        if not text.startswith(f'---\nname: {skill.name}\ndescription: '):
            errors.append(f'{entry.relative_to(root)}: invalid entry metadata')
        portable = 'references/procedure.md' in text
        if portable and len(text.splitlines()) > 28:
            errors.append(f'{skill.name}: entry point exceeds 28 logical lines')
        required_files = ['PROVENANCE.md', 'LICENSE', 'agents/openai.yaml']
        if portable:
            required_files += ['references/procedure.md', 'references/execution-contract.md']
        for required in required_files:
            if not (skill / required).is_file():
                errors.append(f'{skill.name}: missing {required}')
        contract = skill / 'references/execution-contract.md'
        if contract.is_file() and contract.read_bytes() != canonical:
            errors.append(f'{skill.name}: generated contract differs')
        metadata = skill / 'agents/openai.yaml'
        if metadata.is_file():
            fields = {}
            for line in metadata.read_text().splitlines():
                if ': ' in line:
                    key, value = line.strip().split(': ', 1)
                    try:
                        fields[key] = json.loads(value)
                    except ValueError:
                        errors.append(f'{skill.name}: metadata string must be quoted')
            if f'${skill.name}' not in fields.get('default_prompt', ''):
                errors.append(f'{skill.name}: default_prompt missing invocation')
            if not 25 <= len(fields.get('short_description', '')) <= 64:
                errors.append(f'{skill.name}: UI description length outside 25–64')
    for path in root.rglob('*'):
        if '.git' in path.parts or '__pycache__' in path.parts or not path.is_file():
            continue
        if path.suffix not in {'.md', '.json', '.yaml', '.py', '.txt', '.log'}:
            continue
        text = path.read_text()
        if path != rename_notes:
            for old in old_names:
                # Hyphenated legacy names are identifiers; a generic legacy noun
                # is checked only in explicit name/path/invocation contexts.
                if '-' in old:
                    obsolete = old in text
                else:
                    obsolete = any(token in text for token in [
                        f'skills/{old}/', f'/{old}/', f'"{old}"', f"'{old}'",
                        f'name: {old}\n', f'${old}', f'`{old}`'])
                if obsolete:
                    errors.append(f'{path.relative_to(root)}: obsolete skill identifier')
        if path.suffix == '.md':
            if path != rename_notes and old_names:
                titles = '|'.join(re.escape(name.replace('-', ' ').title()) for name in old_names)
                legacy_heading = re.compile(
                    rf'^#{{1,6}}[ \t]+(?:Provenance:[ \t]+)?(?:{titles})[ \t]*#*[ \t]*$',
                    re.MULTILINE)
                for match in legacy_heading.finditer(text):
                    line = text.count('\n', 0, match.start()) + 1
                    errors.append(f'{path.relative_to(root)}:{line}: obsolete skill heading')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in target or target.startswith('#'):
                    continue
                links += 1
                if not (path.parent / target.split('#')[0]).exists():
                    errors.append(f'{path.relative_to(root)}: broken link {target}')
        # Only path-shaped strings; do not embed private source identifiers here.
        machine_roots = tuple('/' + part for part in ['Users/', 'home/', 'private/', 'var/', 'Library/'])
        if any(token in text for token in machine_roots):
            errors.append(f'{path.relative_to(root)}: absolute personal path')
    return errors, len(skills), links


def main():
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/sync_contract.py'), '--check'],
                            capture_output=True, text=True)
    errors, count, links = check()
    if result.returncode:
        errors.append(result.stderr.strip())
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {count} skill packages, {links} local links, metadata, contract copies, and path hygiene.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
