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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import sys
import argparse
import requests
import json
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("name", help="display the github username")
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()

res = requests.get('https://api.github.com/users/' + args.name )
print(res.text)
json = json.loads(res.text)
print(json['avatar_url'])
res2 = requests.get('https://avatars2.githubusercontent.com/u/1023217?v=4', stream=True)

with open(args.name +'.jpg', 'wb') as out_file:
    shutil.copyfileobj(res2.raw, out_file)
del res2
