#!/usr/bin/python# -*- coding: utf-8 -*-
import re

p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
regex = 'http[s]?://(www\.)?([a-z]*\.)*(?P<host>[a-z]*)\.(?P<ext>[a-z]*)?'

m = re.search(p,'http://www.abc.com:123/test')
print(m.group('host')) # 'www.abc.com'
print(m.group('port')) # '123'

m2 = re.search(regex,'http://madrid.elpais.es')
print(m2.group('host')) # 'www.abc.com'
print(m2.group('ext')) # '123'

