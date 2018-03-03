import unittest
import max_pairwise_product
from max_pairwise_product import max_pairwise
import pdb

# pdb.set_trace()

class TestStringMethods(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(max_pairwise([7,5,14,2,8,8,10,1,2,3]), 140)
        self.assertEqual(max_pairwise([1,2,3]), 6)

    def test_two_integers(self):
        self.assertEqual(max_pairwise([1000000,900]), 900000000)

    def test_zero(self):
        self.assertEqual(max_pairwise([1,0]), 0)
        self.assertEqual(max_pairwise([-1,0]), 0)
        self.assertEqual(max_pairwise([0,-2,-1,0]), 0)

    def test_dupes(self):
        self.assertEqual(max_pairwise([3,9,3,7]), 63)
        self.assertEqual(max_pairwise([2,2,1]), 4)

    def test_negatives(self):
        self.assertEqual(max_pairwise([-9, -2, -7]), 14)
        self.assertEqual(max_pairwise([-9, -2, -2]), 4)
