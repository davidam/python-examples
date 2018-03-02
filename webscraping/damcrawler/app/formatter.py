#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata, re

class Formatter(object):

    def __init__(self, s):
        self.string = s

    def imprimes(self):
        print(self.string)
        
    def drop_accents(self):
        result = ""
        thestr = self.string
        for c in unicodedata.normalize('NFD', thestr):
            if (unicodedata.category(c) != 'Mn'):
                result = result + c
        return result

    def drop_whitespaces(self):
        result = ""
        if re.search(r' ', self.string):
            result = re.sub(r' ', '-', self.string)
        return result

    def drop_accents_whitespaces(self):
        result = ""
        thestr = self.string
        # drop accents
        for c in unicodedata.normalize('NFD', thestr):
            if (unicodedata.category(c) != 'Mn'):
                result = result + c
        # drop whitespaces
        if re.search(r' ', result):
            result = re.sub(r' ', '-', result)
        return result

    def hostFromUrl(self):
        url = self.string
        regex = 'http[s]?://(www\.)?([a-z]*\.)*(?P<host>[a-z]*)\.(?P<ext>[a-z]*)?'
        h = re.search(regex,url)
        if hasattr(h, 'group'):
            return h.group('host')
        else:
            return ""

    def isUrl(self):
        url = self.string
        regex = 'http[s]?://(www\.)?([a-z]*\.)*(?P<host>[a-z]*)\.(?P<ext>[a-z]*)?'
        h = ""
        h = re.search(regex,url)
        if hasattr(h, 'group'):
            return True
        else:
            return False

    def isPath(self):
        url = self.string
        regex = '\/.*'
        h = ""
        h = re.search(regex,url)
        if hasattr(h, 'group'):
            return True
        else:
            return False

