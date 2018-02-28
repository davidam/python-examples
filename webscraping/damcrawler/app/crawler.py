#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os, re
from lxml import html


class Crawler(object):

    def __init__(self, s):
        self.url = s
        response = requests.get(self.url)
        tree = html.fromstring(response.text)
        self.title = tree.xpath('//title')[0]
        self.content = response.text
        
    def downloadOneUrl(self, name):
        file = open(name, "w")
        file.write(self.content)
        
    def downloadUrls(self, directory, newspaper):
        if (os.path.exists(directory)):
            os.chdir(directory)
        else:
            os.makedirs(directory)
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        hrefs = tree.xpath('//a//@href')
#        pprint(hrefs)
        for h in hrefs:
            match = re.search(r'http[s]?://(www\.)?([a-z]*\.)?'+newspaper+'\b', h)
            print(match)
            if match:
                print(h)
                c = Crawler(h)
                c.downloadOneUrl("elpais")

c = Crawler("http://www.elpais.es")
#c.downloadOneUrl("tmp1")
c.downloadUrls("/tmp/", "elpais")
#c.downloadUrls("/tmp/", "elpais")
