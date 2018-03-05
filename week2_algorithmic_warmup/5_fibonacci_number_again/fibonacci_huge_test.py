import unittest
from fibonacci_huge import fibonacci_huge
import pdb

PERIOD_LENGTHS = {
    2: 3, 3: 8, 4: 6, 5: 20,
    6: 24, 7: 16, 8: 12, 9: 24, 10: 60
}
class TestStringMethods(unittest.TestCase):

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

        for key, value in PERIOD_LENGTHS.items():
            pisano_period = fibonacci_huge(random_fibonacci_n, key)
            self.assertEqual(len(pisano_period), value)
