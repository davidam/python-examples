import unittest
from app.fib import Fib

class TddInPythonExample(unittest.TestCase):

    def test_fib_fib2_method_returns_correct_result(self):
        f = Fib()
        result = f.fib(2)
        self.assertEqual([1, 1], result)

    def test_fib_fib3_method_returns_correct_result(self):
        f = Fib()
        result = f.fib(3)
        self.assertEqual([1, 1, 2, 3, 5], result)

    def test_fib_fib4_method_returns_correct_result(self):
        f = Fib()
        result = f.fib(4)
        self.assertEqual([1, 1, 2, 3, 5, 8], result)

if __name__ == '__main__':
    unittest.main()
