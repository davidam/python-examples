#!/usr/bin/python
# -*- coding: utf-8 -*-

import newspaper
from newspaper import news_pool
from pprint import pprint

# slate_paper = newspaper.build('http://slate.com')
# tc_paper = newspaper.build('http://techcrunch.com')
# espn_paper = newspaper.build('http://espn.com')
elpais = newspaper.build('http://elpais.com')
elmundo = newspaper.build('http://www.elmundo.es')
publico = newspaper.build('http://www.publico.es')
papers = [elpais, elmundo, publico]
news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
news_pool.join()

print(len(papers))
pprint(papers)
print(len(elpais.articles))
print(len(elmundo.articles))
