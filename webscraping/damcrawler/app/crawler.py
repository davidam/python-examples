#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os, re, hashlib, time, threading
from lxml import html
from app.formatter import Formatter
from app.urlthread import UrlThread
#from formatter import Formatter
from newspaper import Article
#from pprint import pprint

class Crawler(object):

    def __init__(self, s):
        self.url = s
        f = UrlThread(self.url)
        f.start()
        f.join(timeout=10)
        self.title = f.title
        self.content = f.content
        self.urls = [self.url]
        self.files = []
        
    def downloadOneUrl(self, name):
        file = open(name, "w")
        file.write(self.content)
        file.close()
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
        file.close()
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

    def urlsLevelHost(self, level):
        for u in self.urls:
            self.urlsLevel1Host() 
        if (level > 1):
            self.urlsLevelHost(level - 1)
                    
    # def downloadNews(self, level):
    #     self.urlsLevelHost(level)
    #     for u in c.urls:
    #         caux = Crawler(u)
    #         faux = Formatter(u)
    #         name = faux.hostFromUrl() + str(time.time()) + ".html"
    #         caux.downloadOneUrlThread(name)

