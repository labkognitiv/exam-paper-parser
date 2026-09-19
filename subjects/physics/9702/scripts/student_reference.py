#!/usr/bin/env python3
"""Read-only name/alias lookup in Physics's shared student-reference registry.

Results are candidates: the calling skill checks meaning and rechecks under the
write lock before adding an entry. This helper never writes or approves content.
"""
import argparse
import json
from pathlib import Path
import unicodedata


DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / 'study/student-reference/registry.json'


def normalize(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Names and aliases must be nonempty strings')
    text = unicodedata.normalize('NFKC', value).casefold()
    text = text.translate(str.maketrans({'‐': '-', '‑': '-', '–': '-', '—': '-'}))
    return ' '.join(text.split())


def lookup(term, registry_path=DEFAULT_REGISTRY):
    query = normalize(term)
    registry = json.loads(Path(registry_path).read_text(encoding='utf-8'))
    if not isinstance(registry, dict) or registry.get('schema_version') != '9702_student_reference_v1':
        raise ValueError('Unsupported student-reference registry schema')
    entries = registry.get('entries')
    if not isinstance(entries, list):
        raise ValueError('Registry entries must be a list')
    candidates, seen = [], set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError('Each registry entry must be an object')
        identity, payload = entry.get('concept_id'), entry.get('payload')
        if not isinstance(identity, str) or not identity.strip() or identity in seen:
            raise ValueError('Missing or duplicate concept ID')
        seen.add(identity)
        if not isinstance(payload, dict) or not isinstance(payload.get('aliases'), list):
            raise ValueError(f'{identity}: missing payload or aliases list')
        names = [payload.get('term'), *payload['aliases']]
        keys = [normalize(name) for name in names]
        if query in keys:
            candidates.append({
                'concept_id': identity,
                'matched_names': [name for name, key in zip(names, keys) if query == key],
                'payload': payload,
                'payload_sha256': entry.get('payload_sha256'),
                'checks': entry.get('checks'),
                'sources': entry.get('sources', []),
            })
    return {
        'query': term,
        'match': 'none' if not candidates else 'candidate' if len(candidates) == 1 else 'ambiguous',
        'candidates': candidates,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('term', help='Term or known alias, quoted when it contains spaces')
    parser.add_argument('--registry', type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()
    try:
        result = lookup(args.term, args.registry)
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, f'Student-reference lookup failed: {exc}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
