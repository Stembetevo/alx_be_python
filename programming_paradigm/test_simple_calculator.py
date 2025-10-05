import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):

        self.calc = SimpleCalculator()

    def test_addition(self):
      
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 15), 5)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test with floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction(self):
        
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(3, 2), 1)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test with floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    def test_multiplication(self):
       
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 8), 56)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(5, -2), -10)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        
        # Test with floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertEqual(self.calc.divide(15, 5), 3.0)
        
        # Test division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test division by zero (should return None)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test division of zero by non-zero number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        
        # Test division with floating point numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=7)
        
        # Test division resulting in fractions
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        self.assertEqual(self.calc.divide(3, 4), 0.75)


if __name__ == "__main__":
    unittest.main()
