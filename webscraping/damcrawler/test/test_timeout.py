#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from app.timeout import Timeout
from time import sleep

class TddTimeout(unittest.TestCase):
    def test_time_init_method_returns_correct_result(self):
        with Timeout(10):
            sleep(15)
            s = 'No timeout?'
        s = 'Done'
        self.assertEqual(s, 'Done')
