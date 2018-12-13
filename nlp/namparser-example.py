#!/usr/bin/python
# -*- coding: utf-8 -*-

from nameparser import HumanName
name = HumanName("Dr. Juan Q. Xavier de la Vega III (Doc Vega)")
#name
print(name.last)
print(name.as_dict())
print(str(name))
name.string_format = "{first} {last}"
print(str(name))
