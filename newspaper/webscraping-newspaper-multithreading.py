#!/usr/bin/python
# -*- coding: utf-8 -*-

import newspaper
from newspaper import news_pool

slate_paper = newspaper.build('http://slate.com')
tc_paper = newspaper.build('http://techcrunch.com')
espn_paper = newspaper.build('http://espn.com')

papers = [slate_paper, tc_paper, espn_paper]
news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
news_pool.join()

print(slate_paper.articles[10].html)
