#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest, os
from app.crawler import Crawler
 
class TddCrawler(unittest.TestCase):
    def test_formatter_downloadOneUrl_method_returns_correct_result(self):
        c = Crawler("http://www.urjc.es")
        c.downloadOneUrl("urjc.html")
        self.assertEqual(os.path.exists("urjc.html"), True)
                
if __name__ == '__main__':
    unittest.main()
