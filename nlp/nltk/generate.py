#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
grammar = CFG.fromstring(demo_grammar)
print(grammar)
for sentence in generate(grammar, n=10):
     print(' '.join(sentence))

for sentence in generate(grammar, depth=4):
     print(' '.join(sentence))

len(list(generate(grammar, depth=3)))
len(list(generate(grammar, depth=4)))
len(list(generate(grammar, depth=5)))
len(list(generate(grammar, depth=6)))
len(list(generate(grammar)))
