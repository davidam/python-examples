#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: David Arroyo Menéndez
# license: gplv3


import os
f = os.popen('ls -l')
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    if (len(fields) == 2):
        print line
    else:
        megas = int(fields[4]) / 1024
        print(fields[0] + " " + fields[1] + " " + fields[2] + " " + fields[3] + " " + str(megas) + " MB " + fields[5] + " " + fields[6] + " " + fields[7] + " " + fields[8])
