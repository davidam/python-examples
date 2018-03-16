#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print(os.getenv("HOME"))
curpath = os.getcwd()
print(os.getcwd())
os.chdir(os.getenv("HOME"))


