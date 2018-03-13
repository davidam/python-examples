#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, os, re, hashlib, time, threading, pdb, datetime, newspaper
from lxml import html
import xml.etree.cElementTree as ET
from app.formatter import Formatter
from app.urlthread import UrlThread
from newspaper import Article
#from formatter import Formatter
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
        article.download()
        article.parse()        
        file = open(name, "w")
        file.write(article.html)
        file.close()
        self.files.append(name) 

    def downloadOneUrlNewspaperXML(self, name):
        article = Article(self.url)
        article.download()
        article.parse()
        publishDate=article.publish_date.strftime('%Y%m%d') if hasattr(article.publish_date,'strftime') else datetime.datetime.now().strftime('%Y%m%d')
        ID=datetime.datetime.now().strftime('LOG_%Y%m%d-%Hh%Mm')        
        doc = ET.Element("DOC",AUTHOR=article.authors,DATE=publishDate,DOCNO=' ',ID=ID,LNG='ES',SOURCE=article.source_url,URL=article.url)
        ET.SubElement(doc,"TITLE").text = article.title
        ET.SubElement(doc,"SUMMARY").text = article.meta_description #a.summary
        ET.SubElement(doc,"BODY").text = article.text
        ET.SubElement(doc,"IMAGE").text = article.meta_img
        tree = ET.ElementTree(doc)
        tree.write(name,encoding="UTF-8",xml_declaration=True)#,standalone="no",pretty_print=True)
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

