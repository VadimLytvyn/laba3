import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        a, b = 10, 10
        result = self.calculator.add(a, b)
        self.assertEqual(result, 20, "Сума 10 і 10 буде 20")
    
    def test_add_negative_numbers(self):
        a, b = -30, -40
        result = self.calculator.subtract(a, b)
        self.assertEqual(result, -70, "Віднімання -30 і -40 має бути -70")
    unittest.main()
    
calculator = Calculator()
result = calculator.subtract(-30,-40)
print('Віднімання:', result)