import unittest
from b1_sequences import *
class TestB1(unittest.TestCase):
    def test_gc_refactor(self):
        self.assertAlmostEqual(calculate_gc_fraction('ATGCGC'), 4 / 6)
        self.assertAlmostEqual(DNASequence('ATGCGC').gc_fraction(), 4 / 6)
        self.assertAlmostEqual(RNASequence('AUGCGC').gc_fraction(), 4 / 6)
    def test_gc_empty(self):
        with self.assertRaises(ValueError): calculate_gc_fraction('')
    def test_gc_invalid_type(self):
        with self.assertRaises(TypeError): calculate_gc_fraction(None)
    def test_dna(self):
        d = DNASequence('atgcgc'); self.assertEqual(d.sequence, 'ATGCGC'); self.assertEqual(d.length(), 6); self.assertAlmostEqual(d.gc_fraction(), 4/6)
    def test_rna(self):
        self.assertEqual(RNASequence('augcgc').sequence,'AUGCGC')
    def test_protein(self):
        self.assertAlmostEqual(ProteinSequence('MKWVTF').residue_fraction('w'), 1/6)
    def test_nonempty(self):
        for klass in (DNASequence, RNASequence, ProteinSequence):
            with self.subTest(klass=klass), self.assertRaises(ValueError): klass('')
    def test_wrong_symbols(self):
        for klass, seq in ((DNASequence,'AUG'),(RNASequence,'ATG'),(ProteinSequence,'AB')):
            with self.subTest(klass=klass), self.assertRaises(ValueError): klass(seq)
    def test_policy(self):
        with self.assertRaises(ValueError): DNA_POLICY.validate(SequenceData('AUG'))
    def test_type(self):
        with self.assertRaises(TypeError): DNASequence(12)
    def test_symbol(self):
        with self.assertRaises(ValueError): DNASequence('ATGC').count_symbol('GG')
    def test_immutability(self):
        from dataclasses import FrozenInstanceError
        data = SequenceData('ATGC')
        with self.assertRaises(FrozenInstanceError): data.value = 'AAAA'
    def test_polymorphism(self):
        items = [DNASequence('ATGC'), RNASequence('AUGC'), ProteinSequence('MKWV')]
        self.assertEqual([x.length() for x in items], [4,4,4])
        self.assertTrue(all('length=4' in describe_sequence(x) for x in items))
    def test_protein_no_gc(self):
        self.assertFalse(hasattr(ProteinSequence('MKWV'), 'gc_fraction'))
    def test_invalid_fraction_symbol(self):
        with self.assertRaises(ValueError): ProteinSequence('MKWV').residue_fraction('J')
if __name__ == '__main__': unittest.main()
