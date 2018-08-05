#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
import json
from pprint import pprint
#from langdetect import detect
from polyglot.detect import Detector

if __name__=='__main__':

    jsondata = open('perceval-long.json').read()
    json_object = json.loads(jsondata)
    #json = json_object.dumps()
    perceval = json_object["perceval"]
    pprint(json_object)
    print(
    "=======================================================================================" "\n"
    "     Message  Language   \n"
    "   ---------- ---------")

for i in perceval:
    detector = Detector(i['data']['message'])
    print("     %s            %s  " % (i['data']['message'], detector.language))


print("Take care with the json format!!")
