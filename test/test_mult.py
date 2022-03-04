import unittest
from sys import path
path.append('files')
import calc
# from files import calc

class TestCalcMult(unittest.TestCase):

    def test_multiply_pos(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, 1), 1)
        self.assertEqual(calc.multiply(11, 2), 22)

    def test_multiply_neg(self):
        self.assertEqual(calc.multiply(-10, 5), -50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-11, -1), 11)



if __name__ == '__main__':
    unittest.main()
