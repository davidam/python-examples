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
        aux = ""
        thestr = self.string
        for c in unicodedata.normalize('NFD', thestr):
            if (unicodedata.category(c) != 'Mn'):
                aux = aux + c
        if re.search(r' ', self.string):
            aux = re.sub(r' ', '-', self.string)
        return aux

# acentuado = "Balón"    
#f = Formatter("Balón")
# aux = ""
# for c in unicodedata.normalize('NFD', f.string):
#     if (unicodedata.category(c) != 'Mn'):
#         aux = aux + c
# print(aux)
#print(f.drop_accents())
# #result = f.drop_accents()
