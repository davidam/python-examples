# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from pprint import pprint
import requests, random, re, os
from lxml import html
#https://elpais.com/hemeroteca/elpais/2017/01/01/m/portada.html


def downloadOneUrl(url, name):
    res = requests.get(url)
    file = open(name, "w")
    file.write(res.text)

def downloadUrls(url, directory):
    if (os.path.exists(directory)):
        os.chdir(directory)
    else:
        os.makedirs(directory)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    hrefs = tree.xpath('//a//@href')
    pprint(hrefs)
#    match = re.search(r'http[s]?://(www\.)?([a-z]*\.)?elpais\b', h)
    for h in hrefs:
        match = re.search(r'http[s]?://(www\.)?([a-z]*\.)?elpais\b', h)
        if match:                      
            print(h) # match.group() ## 'found word:cat'
            # r = random.randrange(0, 100, 2)
            # downloadOneUrl(h, r)
    #         res = requests.get(url)

    #         file = open("elpais-"+str(r)+".html", "w")
    #         file.write(res.text)

url = 'https://elpais.com/hemeroteca/elpais/2017/01/01/m/portada.html'
downloadOneUrl(url, "elpais-01.html")
downloadUrls(url, "https://elpais.com/hemeroteca/elpais/2017/01/01/m/portada.html")
#downloadUrls(url, "tmp")
        
