#!/usr/bin/env python3
"""Check Almanac Markdown/YAML structure, not horticultural truth or full OKF conformance.

Requires Python 3.10+ and PyYAML. Checks inline Markdown links, reference links,
explicit HTML anchors, ordinary heading fragments, local source paths, claims,
footnotes, quantities, and known typed relations. Fenced examples are ignored.
External URLs are not fetched. Prose/quantity agreement and card usefulness need
editorial review; arbitrary Markdown extensions and attestation are not validated.
"""
import argparse
import math
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
RELATIONS = {
    'classified_as': ({'Crop', 'Cultivar', 'Problem'}, {'Taxon'}),
    'cultivar_of': ({'Cultivar'}, {'Crop'}),
    'applies_to': ({'Procedure', 'Claim'}, {'Crop', 'Cultivar', 'GrowingSystem'}),
    'has_symptom': ({'Problem'}, {'Symptom'}),
    'investigates': ({'Procedure'}, {'Problem', 'Symptom'}),
    'addresses': ({'Procedure'}, {'Problem'}),
    'uses_tool': ({'Procedure', 'MeasurementMethod'}, {'Tool'}),
    'describes_food_from': ({'FoodProfile'}, {'Crop', 'Cultivar'}),
    'estimates_yield_of': ({'YieldEstimate'}, {'Crop', 'Cultivar'}),
    'uses_food_profile': ({'YieldEstimate'}, {'FoodProfile'}),
    'uses_method': ({'YieldEstimate'}, {'MeasurementMethod'}),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prose(body):
    return re.sub(r'^(`{3,}|~{3,}).*?^\1\s*$', '', body, flags=re.M | re.S)


def anchors(body):
    result = set(re.findall(r'<a\s+id=[\"\']([^\"\']+)', body))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', body, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if not count else f'{slug}-{count}')
    return result


def check(root):
    root = root.resolve()
    require(root.is_dir(), f'not a directory: {root}')
    errors, docs = [], {}
    claims_count = links_count = 0
    for path in sorted(root.rglob('*.md')):
        try:
            require(path.resolve().is_relative_to(root), 'document symlink escapes bundle')
            match = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z', path.read_text(), re.S)
            require(match, 'missing YAML frontmatter delimiters')
            meta = yaml.load(match[1], Loader=UniqueLoader)
            require(isinstance(meta, dict), 'frontmatter must be a mapping')
            body = prose(match[2])
            explicit = re.findall(r'<a\s+id=[\"\']([^\"\']+)', body)
            require(len(explicit) == len(set(explicit)), 'duplicate explicit anchor')
            docs[path.resolve()] = (meta, body)
        except (ValueError, yaml.YAMLError, OSError, TypeError) as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')
    require(docs, 'no parseable Markdown documents found')

    def resolve(target, origin):
        nonlocal links_count
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            return None
        raw = unquote(parts.path)
        dest = ((root / raw.lstrip('/')) if raw.startswith('/') else
                (origin.parent / raw if raw else origin)).resolve()
        require(dest.is_relative_to(root), f'path escapes bundle: {target}')
        require(dest.is_file(), f'missing local target: {target}')
        if parts.fragment and dest.suffix == '.md':
            require(dest in docs, f'target is not parseable: {target}')
            require(unquote(parts.fragment) in anchors(docs[dest][1]), f'missing fragment: {target}')
        links_count += 1
        return dest

    for path, (meta, body) in docs.items():
        try:
            destinations = re.findall(r'\]\(<?([^\s)>]+)>?(?:\s+["\'][^\n]*?["\'])?\)', body)
            refs = dict(re.findall(r'^\[([^\]^]+)\]:\s*<?([^\s>]+)>?', body, re.M))
            destinations += list(refs.values())
            for label, ref in re.findall(r'\[([^\]^]+)\]\[([^\]]*)\]', body):
                require((ref or label) in refs, f'undefined reference link: {ref or label}')
            visible = {resolve(u, path) for u in destinations}
            if path.name in {'index.md', 'log.md'}:
                require('type' not in meta, 'reserved document cannot be a concept')
                if 'okf_version' in meta:
                    require(meta['okf_version'] == '0.2', 'unsupported OKF version')
                continue
            require(isinstance(meta.get('type'), str) and meta['type'], 'missing type')
            require(isinstance(meta.get('title'), str) and meta['title'], 'missing title')
            st = meta.get('steelthumb', {})
            require(st.get('ontology_version') == '0.2', 'missing/current ontology_version 0.2 required')
            require(meta.get('status', 'draft') in {'draft', 'stable', 'deprecated'}, 'invalid lifecycle')
            sources = meta.get('sources', [])
            require(isinstance(sources, list), 'sources must be a list')
            ids = set()
            for source in sources:
                require(isinstance(source.get('resource'), str) and source['resource'], 'source lacks resource')
                if 'id' in source:
                    require(isinstance(source['id'], str) and source['id'], 'source ID must be nonempty text')
                    require(source['id'] not in ids, 'duplicate source ID')
                    ids.add(source['id'])
                # External source scopes may be prose under OKF; check explicit local paths only.
                resource = source['resource']
                if resource.startswith(('/', './', '../')) or resource.endswith('.md'):
                    resolve(resource, path)
            defs = re.findall(r'^\[\^([^]]+)\]:', body, re.M)
            used = set(re.findall(r'\[\^([^]]+)\](?!:)', body))
            require(len(defs) == len(set(defs)), 'duplicate footnote definition')
            require(used <= set(defs), f'undefined footnotes: {used - set(defs)}')
            require(set(defs) <= ids, f'footnotes lack source IDs: {set(defs) - ids}')
            seen = set()
            for claim in st.get('claims', []):
                cid = claim.get('id')
                require(isinstance(cid, str) and cid and cid not in seen, 'missing/duplicate claim ID')
                seen.add(cid)
                require(cid in anchors(body), f'claim lacks body anchor: {cid}')
                require(claim.get('kind') in {'descriptive', 'recommendation', 'hypothesis'}, f'invalid claim kind: {cid}')
                require(isinstance(claim.get('statement'), str) and claim['statement'], f'missing statement: {cid}')
                require(isinstance(claim.get('evidence'), list), f'missing evidence list: {cid}')
                for evidence in claim['evidence']:
                    require(evidence.get('source_id') in ids, f'unknown evidence source: {cid}')
                    require(evidence.get('relation') in {'supports', 'contradicts', 'qualifies'}, f'invalid evidence relation: {cid}')
                    require(evidence['source_id'] in used, f'evidence lacks body citation: {cid}')
                if 'quantity' in claim:
                    q = claim['quantity']
                    require(q.get('property') and q.get('unit'), f'quantity lacks property/unit: {cid}')
                    require(('value' in q and 'min' not in q and 'max' not in q) or
                            ('value' not in q and 'min' in q and 'max' in q), f'quantity requires value OR min/max: {cid}')
                    values = [q[k] for k in ('value', 'min', 'max') if k in q]
                    require(all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in values), f'nonfinite/nonnumeric quantity: {cid}')
                    if 'min' in q:
                        require(q['min'] <= q['max'], f'reversed range: {cid}')
                claims_count += 1
            edges = set()
            for edge in st.get('relations', []):
                predicate, target = edge['predicate'], edge['target']
                require((predicate, target) not in edges, 'duplicate typed relation')
                edges.add((predicate, target))
                require(predicate in RELATIONS, f'unknown project predicate: {predicate}')
                dest = resolve(target, path)
                if dest is not None:
                    require(dest in docs, f'relation target must be a concept: {target}')
                    origins, targets = RELATIONS[predicate]
                    require(meta['type'] in origins and docs[dest][0].get('type') in targets, f'invalid relation types: {predicate}')
                    require(dest in visible, f'relation lacks readable link: {target}')
        except (ValueError, TypeError, KeyError, AttributeError) as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')
    return errors, len(docs), claims_count, links_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', type=Path, help='Standalone Almanac OKF bundle directory')
    args = parser.parse_args()
    try:
        errors, docs, claims, links = check(args.bundle)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'ERROR: {exc}\n')
    if errors:
        parser.exit(1, '\n'.join(errors) + '\n')
    print(f'PASS: {docs} documents, {claims} claims, {links} local references. Structural checks only; citation fidelity, card values, usability, and field outcomes require separate review.')


if __name__ == '__main__':
    main()
