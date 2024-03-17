import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self,a,b):
        return a*b
    def devide(self,a,b):
        if b==0:
            raise ValueError("Ділення на нуль не можливе ")
        return a/b
    
    
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
    
    def test_mulyipy_posiyive_numbers(self):
        a,b=10,6
        result=self.calculator.multiply(a,b)
        self.assertAlmostEqual(result,60,"Добуток 10 і 6 має бути 60")
    
    def test_divide_positive_numbers(self):
        a,b=6,2
        result=self.calculator.divide(a,b)
        self.assertEqual(result,3,"Результат ділення має бути 3")
        

    unittest.main()
    
calculator = Calculator()
result = calculator.divide(6,2)
print('Ділення:', result)