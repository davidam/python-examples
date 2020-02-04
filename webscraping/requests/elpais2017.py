# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from pprint import pprint
import requests
from lxml import html
import random
import re
import os
#https://elpais.com/hemeroteca/elpais/2017/01/01/m/portada.html

def downloadUrls(url, directory):
    if (os.path.exists(directory)):
        os.chdir(directory)
    else:
        os.makedirs(directory)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    #This will create a list of prices
    titles = tree.xpath('//div[@class="box-title"]/text()')
    hrefs = tree.xpath('//a//@href')
    for h in hrefs:
        match = re.search(r'http[s]?://(www\.)?elpais\.es\b', h)
        # If-statement after search() tests if it succeeded
        if match:                      
            print(h) # match.group() ## 'found word:cat'
            res = requests.get(url)
            r = random.randrange(0, len(hrefs), 2)
            file = open("elpais-"+str(r)+".html", "w")
            file.write(res.text)


if (os.path.exists('tmp')):
    os.chdir('tmp')
else:
    os.makedirs('tmp')
                        
list = []
for i in range(1, 13):
    if (i < 10):
        i = "0" + str(i)
    for j in range(1, 32):
        if (j < 10):
            j = "0" + str(j)
        url = "https://elpais.com/hemeroteca/elpais/2017/"+str(i)+"/"+str(j)+"/m/portada.html"
        list.append(url)
        res = requests.get(url)
        print("https://elpais.com/hemeroteca/elpais/2017/"+str(i)+"/"+str(j)+"/m/portada.html")
        file = open("elpais-2017-"+str(i)+"-"+str(j)+".html", "w")
        file.write(res.text)
        downloadUrls(url, str(i)+"-"+str(j))

        
#url = 'http://www.elmundo.es'

#downloadUrls(url, "tmp")
        
# url =  'http://www.gnu.org'
# page = requests.get(url)
# soup = BeatifulSoup(page.text, 'html.parser')
