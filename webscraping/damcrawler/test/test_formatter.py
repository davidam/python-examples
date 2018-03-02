#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from app.formatter import Formatter
 
class TddFormatter(unittest.TestCase):

    def test_formatter_drop_accents_method_returns_correct_result(self):
        self.assertEqual("Balon", "Balon")
        
    def test_formatter_drop_accents2_method_returns_correct_result(self):
        f = Formatter("Balon")
        self.assertEqual("Balon", f.string)

    def test_formatter_drop_accents3_method_returns_correct_result(self):
        f = Formatter("Balón")
        res = f.drop_accents()
        self.assertEqual("Balon", res)

    def test_formatter_drop_whitespaces_method_returns_correct_result(self):
        f = Formatter("En un lugar de la Mancha")
        res = f.drop_whitespaces()
        self.assertEqual("En-un-lugar-de-la-Mancha", res)

    def test_formatter_drop_accents_whitespaces_method_returns_correct_result(self):
        f = Formatter("Balón lala")
        res = f.drop_accents_whitespaces()
        self.assertEqual("Balon-lala", res)
        self.assertEqual("balon-lala", res.lower())

    def test_formatter_hostFromUrl_method_returns_correct_result(self):
        f = Formatter("http://www.elpais.es")
        res = f.hostFromUrl()
        f2 = Formatter("http://madrid.elpais.es")
        res2 = f.hostFromUrl()        
        self.assertEqual("elpais", res)
        self.assertEqual("elpais", res2)        

    def test_formatter_isUrl_method_returns_correct_result(self):
        f = Formatter("http://www.elpais.es")
        res = f.isUrl()
        f2 = Formatter("http://madrid.elpais.es")
        res2 = f2.isUrl()
        f3 = Formatter("/noticias.html")
        res3 = f3.isUrl()                
        self.assertEqual(True, res)
        self.assertEqual(True, res2)
        self.assertEqual(False, res3)
        
    def test_formatter_isPath_method_returns_correct_result(self):
        f = Formatter("/noticias.html")
        res = f.isPath()                
        self.assertEqual(True, res)

        
if __name__ == '__main__':
    unittest.main()
