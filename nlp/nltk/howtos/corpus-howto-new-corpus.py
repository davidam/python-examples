#!/usr/bin/pythont
# -*- coding: utf-8 -*-

import nltk
my_corpus = nltk.corpus.PlaintextCorpusReader('/home/davidam/nltk_data/corpora/elpais', '.*\.ES')
print(my_corpus.sents('20180214-12h13m-19-ES')[0])

