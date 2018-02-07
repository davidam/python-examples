#!/usr/bin/env python

import unittest
from app.md5py import MD5

class TddInPythonExample(unittest.TestCase):

    def test_object_program(self):
        m = MD5()
        m.update("1234")
        hexdigest = m.hexdigest()
        self.assertEqual("81dc9bdb52d04dc20036dbd8313ed055", hexdigest)
        
if __name__ == '__main__':
    unittest.main()
