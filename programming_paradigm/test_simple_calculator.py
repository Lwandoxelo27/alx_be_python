import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc =SimpleCalculator()

    def test_addition(self):
        """Test the additional method."""
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-2, 3), 1)
        self.assertEqual(self.calc.addition(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtraction(5, 3), 2)
        self.assertEqual(self.calc.subtraction(-2, 3), -5)
        self.assertEqual(self.calc.subtraction(0, 0), 0)

    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multuplication(4, 5), 20)
        self.assertEqual(self.calc.multiplication(-2, 3), -6)
        self.assertEqual(self.calc.multiplication(0, 5), 0)

    def test_division(self):
        """Test the division method"""
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-6, 3), -2)
        self.assertRaises(ZeroDivisionError, self.calc.division, 10, 0)

if __name__ == '__main__':
    unittest.main()