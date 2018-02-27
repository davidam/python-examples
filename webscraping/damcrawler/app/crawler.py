#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

class Crawler(object):

    def __init__(self, s):
        self.url = s
  
    def downloadOneUrl(self, name):
        res = requests.get(self.url)
        file = open(name, "w")
        file.write(res.text)

#     def downloadOneUrl(url):
#         res = requests.get(url)
#         tree = html.fromstring(res.text)
# #        pprint(tree)
#         title_elem = tree.xpath('//title')[0]
# #        print(title_elem.text_content().lower())

c = Crawler("http://www.urjc.es")
c.downloadOneUrl("urjc")
