import unittest
from app.persona import Persona
from app.persona import Alumno
 
class TddInPythonExample(unittest.TestCase):
 
    def test_p_method_returns_correct_result(self):
        p = Persona("34799461R", "Susana", "Raval")
        result = "34799461R: Raval, Susana"
        self.assertEqual(str(p), result)

    def test_a_method_returns_correct_result(self):
        a = Alumno("46589499T", "Francisco", "Ceballos", "Python")
        result = "46589499T: Ceballos, Francisco (curso :Python)"
        self.assertEqual(str(a), result)

        
if __name__ == '__main__':
    unittest.main()
