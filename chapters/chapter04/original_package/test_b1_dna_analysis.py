# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
"""unittest suite for Chapter 4 B1 canonical exercise."""
import math
import unittest
from b1_dna_analysis import (validate_dna, calculate_gc_fraction,
                             summarize_dna, analyze_sequences)


class DNAFunctionsTest(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(validate_dna('atgc'), 'ATGC')
    def test_gc_general(self):
        self.assertTrue(math.isclose(calculate_gc_fraction('ATGCGC'), 4/6))
    def test_gc_endpoints(self):
        self.assertEqual(calculate_gc_fraction('ATAT'), 0.0)
        self.assertEqual(calculate_gc_fraction('GGCC'), 1.0)
    def test_input_unchanged(self):
        original = 'atgc'; calculate_gc_fraction(original)
        self.assertEqual(original, 'atgc')
    def test_reject_empty(self):
        with self.assertRaises(ValueError): validate_dna('')
    def test_reject_ambiguous(self):
        with self.assertRaises(ValueError): validate_dna('ATNG')
    def test_reject_invalid(self):
        with self.assertRaises(ValueError): validate_dna('ATXG')
    def test_reject_space(self):
        with self.assertRaises(ValueError): validate_dna('AT GC')
    def test_reject_non_string(self):
        with self.assertRaises(TypeError): validate_dna(123)
    def test_summary(self):
        r = summarize_dna('sample_A', 'atgcgc')
        self.assertEqual(r['length'], 6)
        self.assertTrue(math.isclose(r['gc_fraction'], 4/6))
    def test_bad_id(self):
        with self.assertRaises(TypeError): summarize_dna(1, 'ATGC')
        with self.assertRaises(ValueError): summarize_dna('', 'ATGC')
    def test_batch_order(self):
        r=analyze_sequences({'B':'GGCC','A':'ATAT'})
        self.assertEqual([x['sequence_id'] for x in r], ['B','A'])
    def test_fail_fast(self):
        with self.assertRaises(ValueError):
            analyze_sequences({'A':'ATGC','B':'ATNG','C':'GGCC'})
    def test_wrong_batch_type(self):
        with self.assertRaises(TypeError): analyze_sequences(['ATGC'])
    def test_all_gc_in_range(self):
        for seq in ['A','C','G','T','ACGT','GGCC','ATAT']:
            self.assertGreaterEqual(calculate_gc_fraction(seq),0)
            self.assertLessEqual(calculate_gc_fraction(seq),1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
