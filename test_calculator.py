import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(5, 0), "Error: Cannot divide by zero")

    def test_UniGrade(self):
        self.assertEqual(calculator.UniGrade(85), "A")
        self.assertEqual(calculator.UniGrade(65), "B")
        self.assertEqual(calculator.UniGrade(55), "C")
        self.assertEqual(calculator.UniGrade(45), "D")
        self.assertEqual(calculator.UniGrade(30), "F")

if __name__ == '__main__':
    unittest.main()
