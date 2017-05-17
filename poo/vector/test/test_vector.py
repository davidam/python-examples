import unittest
from app.vector import Vector

class TddInPythonExample(unittest.TestCase):

    def test_default_vector_add(self):
        v1 = Vector(3, 2)
        v2 = Vector(2, 3)
        self.assertEqual("Vector (5, 5)", str(v1+v2))

if __name__ == '__main__':
    unittest.main()





    

