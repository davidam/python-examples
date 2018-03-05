#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os, re, hashlib, time, threading
from lxml import html
from app.formatter import Formatter
#from formatter import Formatter
from newspaper import Article

class Crawler(object):

    def __init__(self, s):
        self.url = s
        response = requests.get(self.url)
        tree = html.fromstring(response.text)
        self.title = tree.xpath('//title')[0].text_content()
        self.content = response.text
        self.urls = [self.url]
        self.files = []
        
    def downloadOneUrl(self, name):
        file = open(name, "w")
        file.write(self.content)
        self.files.append(name)
        
    def downloadOneUrlThread(self, name):
        t = threading.Thread(target = self.downloadOneUrl(name))
        t.start()

    def downloadOneUrlNewspaper(self, name):
        article = Article(self.url)
        article.parse()
        article.download()
        file = open(name, "w")
        file.write(article.clean_dom)
        self.files.append(name) 

    def downloadOneUrlNewspaperThread(self, name):
        t = threading.Thread(target = self.downloadOneUrlNewspaper(name))
        t.start()

    def urlsLevel1Host(self, **kwargs):
        if ("url" in kwargs):
            url = kwargs["url"]
        else:
            url = self.url
        f = Formatter(url)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        hrefs = tree.xpath('//a//@href')
        regex = '^http[s]?://(www\.)?([a-z]*\.)?'+f.hostFromUrl()
        for h in hrefs:
            if h not in self.urls:
                match = re.search(regex, h)
                if match:
                    self.urls.append(h)

#     def urlsLevelHost(self, level):
#         for u in self.urls:
#             print(u)
#             self.urlsLevel1Host(url=u)

# c = Crawler("http://www.elpais.es")
# #c.urlsLevel1Host(url=c.url)
# c.urlsLevelHost(1)
# #print(c.urls)
