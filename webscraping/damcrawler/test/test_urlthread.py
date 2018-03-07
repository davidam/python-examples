#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest, os, threading
from app.urlthread import UrlThread
 
class TddUrlThread(unittest.TestCase):
    def test_urlthread_fetch_method_returns_correct_result(self):
        f = UrlThread("http://www.gnu.org")
        f.start()
        f.join()
        self.assertEqual(f.url, "http://www.gnu.org")
        self.assertEqual(f.title, "The GNU Operating System and the Free Software Movement")        
        self.assertEqual(len(f.hrefs)>1, True)
        
    def test_urlthread_fetch15_method_returns_correct_result(self):
        f = UrlThread("http://www.gnu.org")
        f.start()
        f.join(timeout=15)
        self.assertEqual(f.url, "http://www.gnu.org")
        self.assertEqual(f.title, "The GNU Operating System and the Free Software Movement")        
        self.assertEqual(len(f.hrefs)>1, True)
