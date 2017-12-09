#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rdflib
g=rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')

for s,p,o in g:
    print s,p,o
