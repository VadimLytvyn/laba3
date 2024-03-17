import unittest

class Calculator():
    def power(self,a,b):
        return a**b
    
class TestCalculator():
    def test_calculator_power(self):
        calculator=Calculator()
        self.assertEqual(calculator.power(6,3),216)
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
if __name__=="__main__":
    unittest.main()
    
calculator=Calculator()
result=calculator(6,3)
print("Резултат:")