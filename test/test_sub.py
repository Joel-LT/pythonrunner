import unittest
from sys import path
path.append('files')
import calc
# from files import calc

class TestCalcSub(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)



if __name__ == '__main__':
    unittest.main()
