import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

  def setUp(self):
    """Set up the SimpleCalculator instance before each test."""
    self.calc = SimpleCalculator()

  def test_addition(self):
    """Test the addition method with various inputs."""
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(10.5, 2.2), 12.7)
    self.assertEqual(self.calc.add(0, 0), 0)  # Test adding zero

  def test_subtraction(self):
    """Test the subtraction method with various inputs."""
    self.assertEqual(self.calc.subtract(5, 2), 3)
    self.assertEqual(self.calc.subtract(10, -2), 12)
    self.assertEqual(self.calc.subtract(3.14, 1.5), 1.64)
    self.assertEqual(self.calc.subtract(0, 0), 0)  # Test subtracting zero

  def test_multiplication(self):
    """Test the multiplication method with various inputs."""
    self.assertEqual(self.calc.multiply(2, 3), 6)
    self.assertEqual(self.calc.multiply(-1, 5), -5)
    self.assertEqual(self.calc.multiply(4.2, 1.5), 6.3)
    self.assertEqual(self.calc.multiply(1, 0), 0)  # Test multiplying by zero

  def test_division(self):
    """Test the division method with various inputs."""
    self.assertEqual(self.calc.divide(10, 2), 5)
    self.assertEqual(self.calc.divide(-6, 2), -3)
    self.assertEqual(self.calc.divide(3.5, 1.75), 2)
    self.assertIsNone(self.calc.divide(10, 0))  # Test division by zero

if __name__ == "__main__":
  unittest.main()