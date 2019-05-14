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

def DFS(edges, s, t, skip = []):
   if(s == t):
      return [s]
   if s not in edges: return []
   skip.append(s)
   for x in edges[s]:
       if x in skip: continue
       res = DFS(edges, x, t, skip)
       if(res):
           way = [s]
           way.extend(res)
           return way
   return []


edges = {'a':['b','c'],
         'c':['d','e'],
         'd':['f'],
         'f':['c'],
         'e':['f','g']}

way = DFS(edges, 'a', 'e')
if way:
  print(', '.join(map(str, way)))
else:
  print('No way')
