import unittest
from app.calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_sub_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.sub(2,2)
        self.assertEqual(0, result)

        
    def test_calculator_prod_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.prod(2,2)
        self.assertEqual(4, result)
        
    def test_calculator_div_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.div(2,2)
        self.assertEqual(1, result)

        
if __name__ == '__main__':
    unittest.main()
