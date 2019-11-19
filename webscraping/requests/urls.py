#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with urls; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# This program returns a list of broken links in an url

import requests
from lxml import html
from pprint import pprint
import os,re

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="url to analize broken links")
args = parser.parse_args()


start_url = args.url
response = requests.get(start_url)
tree = html.fromstring(response.text)
links = tree.cssselect('a')  # or tree.xpath('//a')

out = []
for link in links:
    # we use this if just in case some <a> tags lack an href attribute
    if 'href' in link.attrib:
        out.append(link.attrib['href'])

absoluteurls = []
for o in out:
    if 'http' in o:
        print(o)
        absoluteurls.append(o)
    else:
        o = start_url + '/' + o
        print(o)
        absoluteurls.append(o)

buggyurls = []
for l in absoluteurls:
    print(l)
    try:
        r = requests.get(l)
        r.raise_for_status()
        print(r.status_code)
    except:
        buggyurls.append(l)
        print("Error")

print("Urls with troubles:")
print(buggyurls)
