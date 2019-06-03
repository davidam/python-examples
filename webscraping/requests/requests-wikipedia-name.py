#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html

#r = requests.get('http://localhost/maria.html')
r = requests.get('https://es.wikipedia.org/wiki/María_(nombre)')

print(r.url)
#print(r.text)


tree = html.fromstring(r.content)

gender = tree.xpath('//a[@title="Identidad sexual"]/text()')
mariagender = tree.xpath('//div[@class="mw-parser-output"]//table//tbody//td//text()')
footer = tree.xpath('//div[@class="action-list"]//p/text()')

print(gender)
print(mariagender[5])
