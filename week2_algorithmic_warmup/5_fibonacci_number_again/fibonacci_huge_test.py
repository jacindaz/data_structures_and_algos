import unittest
from fibonacci_huge import fibonacci_huge
from fibonacci_huge import find_pisano_period_length
import pdb

class TestFibonacciHuge(unittest.TestCase):
    PERIOD_LENGTHS = {
        2: 3, 3: 8, 4: 6, 5: 20,
        6: 24, 7: 16, 8: 12, 9: 24, 10: 60,
        11: 10, 12: 24, 13: 28, 14: 48, 15: 40,
        16: 24, 17: 36, 18: 24, 19: 18,
        20: 60, 21: 16, 22: 30, 23: 48, 24: 24,
    }

    PERIOD_VALUES = {
        2: '011', 3: '01120221', 4: '011231', 5: '01123033140443202241',
        6: '011235213415055431453251',
        7: '0112351606654261',
        8: '011235055271',
        9: '011235843718088764156281',
        10: '011235831459437077415617853819099875279651673033695493257291'
    }

    def test_period_length(self):
        random_fibonacci_n = 500

        for modulo, expected_period_length in self.PERIOD_LENGTHS.items():
            pisano_period = find_pisano_period_length(random_fibonacci_n, modulo)
            self.assertEqual(pisano_period, expected_period_length)

    def test_larger_peroid_lengths(self):
        lengths = {
            109: 108, 110: 60, 111: 152, 112: 48, 113: 76,
            114: 72, 115: 240, 116: 42, 117: 168, 118: 174,
            119: 144, 120: 120
        }
        random_fibonacci_n = 500

        for modulo, expected_period_length in lengths.items():
            pisano_period = find_pisano_period_length(random_fibonacci_n, modulo)
            self.assertEqual(pisano_period, expected_period_length)

    def test_fibonacci_huge(self):
        expected_results = [
            { 'fib': 2015, 'mod': 3, 'result': 1 },
            { 'fib': 239, 'mod': 1000, 'result': 161 },
            # { 'fib': 2816213588, 'mod': 30524, 'result': 10249 }
        ]
        random_fibonacci_n = 500

        for expected_result in expected_results:
            results = fibonacci_huge(expected_result['fib'], expected_result['mod'])
            self.assertEqual(results, expected_result['result'])
