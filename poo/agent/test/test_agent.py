import unittest
from app.agent import Agent, Object
 
class TddInPythonExample(unittest.TestCase):

    def test_object_program(self):
        o = Object()
        self.assertEqual(False, o.is_alive())
    
    def test_agent_program(self):
        a = Agent()
        self.assertEqual(True, a.alive)        
        
if __name__ == '__main__':
    unittest.main()
