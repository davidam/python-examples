#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, threading
from lxml import html

class UrlThread(threading.Thread):

    def __init__(self, s):
        self.url = s
        threading.Thread.__init__(self)        
        self.hrefs = []
        self.title = ""
        self.content = ""
        
    def run(self):
        response = requests.get(self.url)
        tree = html.fromstring(response.text)
        self.hrefs = tree.xpath('//a//@href')
        self.title = tree.xpath('//title')[0].text_content()
        self.content = response.text




