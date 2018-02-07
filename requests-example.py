#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests

r = requests.get('https://api.github.com/users/davidam/repos')
print(r.url)
print(r.text)

