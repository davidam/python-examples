#!/usr/bin/env python
# author: David Arroyo Menéndez
# license: gplv3

import os
f = os.popen('cat /proc/meminfo')
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    if (len(fields) < 3):
        print(str(fields[0]) + " "  + str(fields[1]))
    else:
        if fields[2] == "kB":
            megas = int(fields[1]) / 1024
            print(str(fields[0]) + " " + str(megas) + " MB")
