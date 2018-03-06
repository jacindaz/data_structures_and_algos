import unittest
from fibonacci import fibonacci
import pdb

class TestFibonacciHuge(unittest.TestCase):
    def test_fibonacci(self):
        fib_values = {
            10: 55,
            17: 1597,
            43: 433494437,
            100: 354224848179261915075,
            239: 39679027332006820581608740953902289877834488152161,
            589: 554926040554257829308125788274680482815955849738659889938144313725789769599132698259438063468312512862179152906263350659689
        }

        for fibonacci_n, expected_fib in fib_values.items():
            self.assertEqual(fibonacci(fibonacci_n), expected_fib)
