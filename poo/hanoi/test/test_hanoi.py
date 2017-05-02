import unittest
from app.hanoi import Hanoi
 
class TddInPythonExample(unittest.TestCase):
 
    def test_hanoi3_method_returns_correct_result(self):
        h = Hanoi()
        result = h.hanoi(3)
        self.assertEqual(7, result)

    def test_hanoi4_method_returns_correct_result(self):
        h = Hanoi()
        result = h.hanoi(4)
        self.assertEqual(15, result)
        
        
if __name__ == '__main__':
    unittest.main()
