"""Regression tests for stale review detection; no automated truth judgments."""
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path
import yaml
from check_fidelity import check, digest


class FidelityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.claim = {'id': 'depth', 'statement': 'Scoped planting depth',
                      'evidence': [{'source_id': 'original', 'locator': 'Planting'}]}
        self.data = {'sources': [{'id': 'original', 'resource': 'https://example.org/source'}],
                     'steelthumb': {'claims': [self.claim]}}
        self.write()
        self.ledger = {'documents': [{'entity': 'crop.md', 'sha256': hashlib.sha256((self.root / 'crop.md').read_bytes()).hexdigest()}],
                       'claims': [{'entity': 'crop.md', 'claim_id': 'depth', 'claim_sha256': digest(self.claim),
                                   'verdict': 'supports-with-scope', 'rationale': 'Manual comparison',
                                   'passages': [{'source_id': 'original', 'url': 'https://example.org/source',
                                                 'locator': 'Planting', 'accessed': '2026-09-27'}]}]}

    def write(self, body='Body'):
        (self.root / 'crop.md').write_text('---\n' + yaml.safe_dump(self.data) + '---\n' + body)

    def test_current_review(self):
        self.assertEqual(check(self.root, self.ledger)[0], [])

    def test_changed_claim(self):
        self.claim['statement'] = 'Different recommendation'
        self.write()
        self.assertTrue(any('Stale claim' in e for e in check(self.root, self.ledger)[0]))

    def test_changed_prose(self):
        self.write('Changed guidance')
        self.assertTrue(any('document' in e for e in check(self.root, self.ledger)[0]))

    def test_changed_source(self):
        self.data['sources'][0]['resource'] = 'https://example.org/different'
        self.write()
        self.assertTrue(any('Source mismatch' in e for e in check(self.root, self.ledger)[0]))

    def test_missing_review(self):
        self.ledger['claims'] = []
        self.assertTrue(any('Missing claim review' in e for e in check(self.root, self.ledger)[0]))

    def test_uninspected_edge(self):
        self.claim['evidence'].append({'source_id': 'second', 'locator': 'Methods'})
        self.data['sources'].append({'id': 'second', 'resource': 'https://example.org/second'})
        self.write()
        self.assertTrue(any('Unaccounted evidence' in e for e in check(self.root, self.ledger)[0]))


if __name__ == '__main__':
    unittest.main()
