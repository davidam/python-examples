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
        regex = 'http[s]?://(www\.)?([a-z]*)?\.([a-z]*)?'
        host = re.sub(regex, r'\2', url)
        return host

    
# # acentuado = "Balón"    
# f = Formatter("Balón lala")
# # aux = ""
# # for c in unicodedata.normalize('NFD', f.string):
# #     if (unicodedata.category(c) != 'Mn'):
# #         aux = aux + c
# # print(aux)
# print(f.drop_accents_whitespaces())
# # #result = f.drop_accents()
