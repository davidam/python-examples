#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.book import *

saying = ['After', 'all', 'is', 'said', 'and', 'done',
          'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
print(tokens[-2:])
print(tokens)

fdist1 = FreqDist(text1)
print(fdist1)
fdist1.most_common(50)
print(fdist1['whale'])
