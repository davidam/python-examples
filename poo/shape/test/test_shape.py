import unittest
from app.shape import Shape
 
class TddInPythonExample(unittest.TestCase):
 
    def test_shape_area_method_returns_correct_result(self):
        s = Shape(5, 4)
        result = s.area()
        self.assertEqual(20, result)

    def test_shape_perimeter_method_returns_correct_result(self):
        s = Shape(3, 2)
        result = s.perimeter()
        self.assertEqual(10, result)
    
if __name__ == '__main__':
    unittest.main()
