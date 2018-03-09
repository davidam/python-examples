#!/usr/bin/python
# -*- coding: utf-8 -*-
from formatter import Formatter
from urlthread import UrlThread
from formatter import Formatter
from crawler import Crawler
from newspaper import Article
import os
#import pdb
from pprint import pprint
import time


if __name__ == "__main__":
    year = 2017
    month = 13
    day = 32

    m = []
#    pdb.set_trace()
    for i in range(1, month):
        if (i < 10):    
            m.append(["0"+str(i)])
            mstr = "0"+str(i)
        else:
            m.append([i])
            mstr = str(i)
        d = []
        curpath = "/tmp/"
        os.chdir(curpath)
        for j in range(1, day):
            if (j < 10):
                d.append(["0"+str(j)])
                dstr = "0"+str(j)            
            else:
                d.append([j])
                dstr = str(j)
            url = "https://elpais.com/hemeroteca/elpais/2017/"+mstr+"/"+dstr+"/m/portada.html"
            print(url)
            path = mstr+"-"+dstr
            if (os.path.isdir(path)):
                print("Path is created")
            else:
                os.makedirs(path)
            os.chdir(path)
            
            c = Crawler(url)
            c.urlsLevelHost(2)
            for u in c.urls:
                caux = Crawler(u)
                faux = Formatter(u)
                name = faux.hostFromUrl() + str(time.time())
                caux.downloadOneUrlThread(name)
            os.chdir(curpath)

