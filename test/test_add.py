import unittest
from sys import path
path.append('files')
import calc
# from files import calc
class TestCalcAdd(unittest.TestCase):
    
    def test_add_pos(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, 1), 2)
        self.assertEqual(calc.add(11, 1), 12)
    
    def test_add_neg(self):
        self.assertEqual(calc.add(-10, 5), -5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

class TestCalcAddLarge(unittest.TestCase):
    
    def test_add_pos_large(self):
        self.assertEqual(calc.add(1000, 5), 1005)
        self.assertEqual(calc.add(1000, 1), 1001)
        self.assertEqual(calc.add(11, 1), 12)
    
    def test_add_neg_large(self):
        self.assertEqual(calc.add(-1000, 5), -995)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()
