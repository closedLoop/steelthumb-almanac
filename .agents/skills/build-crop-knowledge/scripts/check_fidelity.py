#!/usr/bin/env python3
"""Check citation-review coverage and staleness, not whether sources are true.

Python 3 + PyYAML. The JSON ledger is a contributor working-tree audit, not OKF
verification metadata. A reviewer must inspect passages and record verdicts.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import yaml


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':')).encode()).hexdigest()


def check(bundle, ledger):
    errors = []
    claims = {}
    documents = {}
    for path in sorted(bundle.rglob('*.md')):
        rel = path.relative_to(bundle).as_posix()
        raw = path.read_bytes()
        documents[rel] = hashlib.sha256(raw).hexdigest()
        data = yaml.safe_load(raw.decode().split('---', 2)[1])
        source_map = {s.get('id'): s.get('resource') for s in data.get('sources', [])}
        for claim in data.get('steelthumb', {}).get('claims', []):
            claims[(rel, claim['id'])] = (claim, source_map)
    recorded_documents = {d['entity']: d['sha256'] for d in ledger['documents']}
    if len(recorded_documents) != len(ledger['documents']):
        errors.append('Duplicate document records')
    for rel in sorted(documents.keys() | recorded_documents.keys()):
        if documents.get(rel) != recorded_documents.get(rel):
            errors.append(f'Stale, missing or removed document: {rel}')
    seen = set()
    counts = {}
    for row in ledger['claims']:
        key = (row['entity'], row['claim_id'])
        if key in seen:
            errors.append(f'Duplicate claim review: {key}')
        seen.add(key)
        if key not in claims:
            errors.append(f'Review refers to removed claim: {key}')
            continue
        claim, sources = claims[key]
        if digest(claim) != row['claim_sha256']:
            errors.append(f'Stale claim review: {key}')
        verdict = row['verdict']
        if verdict not in {'pending', 'supports-with-scope', 'contradicts', 'unresolved'}:
            errors.append(f'Unknown verdict: {key}: {verdict}')
        counts[verdict] = counts.get(verdict, 0) + 1
        if verdict != 'pending':
            if not row.get('rationale') or not row.get('passages'):
                errors.append(f'Missing reasoning or passages: {key}')
            evidence_ids = {e['source_id'] for e in claim['evidence']}
            inspected = set()
            for passage in row.get('passages', []):
                sid = passage.get('source_id')
                inspected.add(sid)
                if sources.get(sid) != passage.get('url') or sid not in evidence_ids:
                    errors.append(f'Source mismatch: {key}: {sid}')
                if not passage.get('locator') or not passage.get('accessed'):
                    errors.append(f'Missing locator/access date: {key}: {sid}')
            if evidence_ids - inspected:
                errors.append(f'Unaccounted evidence edges: {key}')
    for key in sorted(claims.keys() - seen):
        errors.append(f'Missing claim review: {key}')
    return errors, counts, len(documents)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('bundle', type=Path)
    p.add_argument('ledger', type=Path)
    p.add_argument('--require-complete', action='store_true',
                   help='Fail if any claim is pending, unresolved or contradicted; still not a truth check.')
    args = p.parse_args()
    errors, counts, documents = check(args.bundle, json.loads(args.ledger.read_text()))
    for error in errors:
        print(error, file=sys.stderr)
    print(f'{documents} document snapshots; claim verdicts: {counts}')
    print('Ledger consistency only. Passage judgments are manual; prose and card review have separate scope.')
    incomplete = any(counts.get(v, 0) for v in ('pending', 'unresolved', 'contradicts'))
    return 1 if errors or (args.require_complete and incomplete) else 0


if __name__ == '__main__':
    raise SystemExit(main())
