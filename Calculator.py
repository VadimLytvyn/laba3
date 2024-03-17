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