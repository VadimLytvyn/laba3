import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        a, b = 10, 10
        result = self.calculator.add(a, b)
        self.assertEqual(result, 20, "Сума 10 і 10 буде 20")
        
    unittest.main()
    
calculator = Calculator()
result = calculator.add(10,10)
print('Додавання:', result)