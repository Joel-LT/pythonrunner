import unittest
from sys import path
path.append('files')
import calc
# from files import calc

class TestCalcDiv(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        # self.assertEqual(calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
