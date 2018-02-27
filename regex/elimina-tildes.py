#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

print(elimina_tildes("córcholis"))
