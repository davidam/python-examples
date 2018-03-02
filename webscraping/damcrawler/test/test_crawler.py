#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest, os, threading
from app.crawler import Crawler
 
class TddCrawler(unittest.TestCase):
    def test_crawler_downloadInit_method_returns_correct_result(self):
        c = Crawler("http://www.gnu.org")
        self.assertEqual(c.url, "http://www.gnu.org")
        self.assertEqual(c.title, "The GNU Operating System and the Free Software Movement")        

    def test_crawler_downloadOneUrl_method_returns_correct_result(self):
        c = Crawler("http://www.urjc.es")
        c.downloadOneUrl("urjc.html")
        self.assertEqual(os.path.exists("urjc.html"), True)
        
    def test_crawler_downloadOneUrlThread_method_returns_correct_result(self):
        c = Crawler("http://www.elpais.es")
        c.downloadOneUrlThread("elpais.html")
        self.assertEqual(os.path.exists("elpais.html"), True)

    def test_crawler_downloadOneUrlNewspaper_method_returns_correct_result(self):
        c = Crawler("https://politica.elpais.com/politica/2017/08/29/actualidad/1504006030_167758.html")
        c.downloadOneUrl("alienigenaviolanenes.html")
        self.assertEqual(os.path.exists("alienigenaviolanenes.html"), True)
        
    def test_crawler_downloadOneUrlNewspaperThread_method_returns_correct_result(self):
        c = Crawler("https://politica.elpais.com/politica/2017/08/29/actualidad/1504006030_167758.html")
        c.downloadOneUrlThread("alienigenaviolanenes.html")
        self.assertEqual(os.path.exists("alienigenaviolanenes.html"), True)

    def test_crawler_urlsLevel1Host_method_returns_correct_result(self):   
        c = Crawler("http://www.elpais.es")
        c.urlsLevel1Host()
        self.assertEqual(len(c.urls)>1, True)
        
if __name__ == '__main__':
    unittest.main()
