import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
<<<<<<< Updated upstream
    def multiply(self,a,b):
        return a*b
    def devide(self,a,b):
        if b==0:
            raise ValueError("Ділення на нуль не можливе ")
        return a/b
    
=======
>>>>>>> Stashed changes
    
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
<<<<<<< Updated upstream
    
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
import unittest

class Calculator():
    def power(self,a,b):
        return a**b
    
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a

    def lcm(self,a,b):
        return a*b//self.gcd(a,b)
     
class TestCalculator():
    def test_calculator_power(self):
        calculator=Calculator()
        self.assertEqual(calculator.power(6,3),216)
    def test_gcd(self):
        calculator=Calculator()
        self.assertEqual(calculator.gcd(12,18),6)
        self.assertEqual(calculator.gcd(15,25),5)
        self.assertEqual(calculator.gcd(21,18),7)
        
    def test_lcm(self):
        calculator=Calculator()
        self.assertEqual(calculator.gcd(12,18),36)
        self.assertEqual(calculator.gcd(15,25),75)
        self.assertEqual(calculator.gcd(21,28),84)
    
if __name__=="__main__":
    unittest.main()
    
calculator=Calculator()
result=calculator(6,3)
print("Резултат:")
=======
    unittest.main()
    
calculator = Calculator()
result = calculator.subtract(-30,-40)
print('Віднімання:', result)
>>>>>>> Stashed changes
