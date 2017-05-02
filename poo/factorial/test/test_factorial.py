import unittest
from app.factorial import Factorial
 
class TddInPythonExample(unittest.TestCase):
 
    def test_factorial_fac2_method_returns_correct_result(self):
        f = Factorial()
        result = f.fac(2)
        self.assertEqual(2, result)

    def test_factorial_fac3_method_returns_correct_result(self):
        f = Factorial()
        result = f.fac(3)
        self.assertEqual(6, result)

        
    def test_calculator_fac4_method_returns_correct_result(self):
        f = Factorial()
        result = f.fac(4)
        self.assertEqual(24, result)

    
if __name__ == '__main__':
    unittest.main()
