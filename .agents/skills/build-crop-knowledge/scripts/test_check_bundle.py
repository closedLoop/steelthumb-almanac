"""Regression tests for evidence integrity and portable bundle boundaries."""
import tempfile
import unittest
from pathlib import Path

from check_bundle import check


DOC = '''---
type: Crop
title: Synthetic checker fixture
status: draft
sources:
- id: source
  resource: https://example.invalid/fixture
steelthumb:
  ontology_version: '0.2'
  future_extension: retained
  claims:
  - id: setting
    kind: hypothesis
    statement: Synthetic value for checker testing only.
    evidence:
    - source_id: source
      relation: supports
      locator: Synthetic fixture
    quantity:
      property: synthetic_interval
      min: 1
      max: 2
      unit: d
---
# Synthetic checker fixture

<a id="setting"></a>
Synthetic statement.[^source]

[Own claim](#setting)

[^source]: [Synthetic source](https://example.invalid/fixture).
'''


class BundleChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'bundle'
        self.root.mkdir()
        self.doc = self.root / 'fixture.md'
        self.doc.write_text(DOC)

    def errors(self, text):
        self.doc.write_text(text)
        return '\n'.join(check(self.root)[0])

    def test_valid_bundle_and_unknown_metadata_are_accepted(self):
        self.assertEqual(check(self.root)[0], [])
        self.assertIn('future_extension: retained', self.doc.read_text())

    def test_missing_source_join_is_rejected(self):
        self.assertIn('unknown evidence source', self.errors(DOC.replace('source_id: source', 'source_id: absent')))

    def test_broken_claim_anchor_is_rejected(self):
        self.assertIn('missing fragment', self.errors(DOC.replace('id="setting"', 'id="changed"')))

    def test_existing_file_outside_bundle_is_rejected(self):
        (self.root.parent / 'secret.md').write_text('outside')
        self.assertIn('escapes bundle', self.errors(DOC + '\n[Outside](../secret.md)\n'))

    def test_symlink_escape_is_rejected(self):
        (self.root.parent / 'outside.txt').write_text('outside')
        (self.root / 'alias.txt').symlink_to(self.root.parent / 'outside.txt')
        self.assertIn('escapes bundle', self.errors(DOC + '\n[Alias](alias.txt)\n'))

    def test_duplicate_yaml_key_is_rejected(self):
        # Include another valid file so diagnostics remain available after parse failure.
        (self.root / 'valid.md').write_text(DOC)
        self.assertIn('duplicate YAML key', self.errors(DOC.replace('type: Crop', 'type: Crop\ntype: Procedure')))

    def test_reversed_or_ambiguous_quantity_is_rejected(self):
        self.assertIn('reversed range', self.errors(DOC.replace('min: 1', 'min: 3')))
        self.assertIn('value OR min/max', self.errors(DOC.replace('min: 1', 'value: 1\n      min: 1')))

    def test_wrong_relation_type_is_rejected(self):
        text = DOC.replace('  claims:', '  relations:\n  - predicate: cultivar_of\n    target: /fixture.md\n  claims:')
        self.assertIn('invalid relation types', self.errors(text))

    def test_undefined_footnote_is_rejected(self):
        self.assertIn('undefined footnotes', self.errors(DOC.replace('statement.[^source]', 'statement.[^absent]')))

    def test_fenced_examples_do_not_create_live_links(self):
        self.assertEqual(self.errors(DOC + '\n```md\n[Example](missing.md)\n```\n'), '')


if __name__ == '__main__':
    unittest.main()
