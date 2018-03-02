#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os, re, hashlib, time, threading
from lxml import html
from app.formatter import Formatter
from newspaper import Article

class Crawler(object):

    def __init__(self, s):
        self.url = s
        response = requests.get(self.url)
        tree = html.fromstring(response.text)
        self.title = tree.xpath('//title')[0].text_content()
        self.content = response.text
        self.urls = []
        
    def downloadOneUrl(self, name):
        file = open(name, "w")
        file.write(self.content)
        
    def downloadOneUrlThread(self, name):
        t = threading.Thread(target = self.downloadOneUrl(name))
        t.start()

    def downloadOneUrlNewspaper(self, name):
        article = Article(self.url)
        article.parse()
        article.download()
        file = open(name, "w")
        file.write(article.clean_dom)

    def downloadOneUrlNewspaperThread(self, name):
        t = threading.Thread(target = self.downloadOneUrlNewspaper(name))
        t.start()

    def urlsLevel1Host(self):
        f = Formatter(self.url)
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        hrefs = tree.xpath('//a//@href')
        regex = 'http[s]?://(www\.)?([a-z]*\.)?'+f.hostFromUrl()
        for h in hrefs:
            if h not in self.urls:
                match = re.search(regex, h)
                if match:
                    self.urls.append(h)
                
    # def urlsLevel1Host(self, host, url):
    #     page = requests.get(self.url)
    #     tree = html.fromstring(page.content)
    #     hrefs = tree.xpath('//a//@href')
    #     regex = 'http[s]?://(www\.)?([a-z]*\.)?'+host
    #     for h in hrefs:
    #         if h not in self.urls:
    #             match = re.search(regex, h)
    #             if match:
    #                 print(h)
    #                 self.urls.append(h)
                    
    # def urlsLevelHost(self, level, host):
    #     for u in self.urls:
    #         self.urlsLevel1Host(host) 
    #     if (level > 1):
    #         self.urlsLevelHost(level - 1, host)

        
    # def downloadUrls(self, directory, newspaper):
    #     if (os.path.exists(directory)):
    #         os.chdir(directory)
    #     else:
    #         os.makedirs(directory)
    #     page = requests.get(self.url)
    #     tree = html.fromstring(page.content)
    #     hrefs = tree.xpath('//a//@href')
    #     regaux = 'http[s]?://(www\.)?([a-z]*\.)?'+newspaper
    #     for h in hrefs[0:15]:
    #         match = re.search(regaux, h)
    #         if match:
    #             print(h)
    #             f = Formatter(self.title)
    #             t = f.drop_accents_whitespaces().lower() + str(time.time())
    #             print(t)
    #             cc = Crawler(h)
    #             cc.downloadOneUrl(t +".html")

# c = Crawler("http://www.elpais.es")
# c.downloadOneUrl("elpais.html")
# c.downloadUrls("/tmp/","elpais")

#print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
