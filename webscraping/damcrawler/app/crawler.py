#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os, re, hashlib, time, threading
from lxml import html
from formatter import *

class Crawler(object):

    def __init__(self, s):
        self.url = s
        response = requests.get(self.url)
        tree = html.fromstring(response.text)
        self.title = tree.xpath('//title')[0].text_content()
        self.content = response.text
        
    def downloadOneUrl(self, name):
        file = open(name, "w")
        file.write(self.content)

    def downloadOneUrlThread(self, name):
        t = threading.Thread(target = self.downloadOneUrl(name))
        t.start()        
        
    def downloadUrls(self, directory, newspaper):
        if (os.path.exists(directory)):
            os.chdir(directory)
        else:
            os.makedirs(directory)
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        hrefs = tree.xpath('//a//@href')
        regaux = 'http[s]?://(www\.)?([a-z]*\.)?'+newspaper
        for h in hrefs[0:15]:
            match = re.search(regaux, h)
            if match:
                print(h)
                f = Formatter(self.title)
                t = f.drop_accents_whitespaces().lower() + str(time.time())
                print(t)
                cc = Crawler(h)
                cc.downloadOneUrl(t +".html")

# c = Crawler("http://www.elpais.es")
# c.downloadOneUrl("elpais.html")
# c.downloadUrls("/tmp/","elpais")
