#!/usr/bin/python
# -*- coding: utf-8 -*-
# Print strings from a file

import sys
import re

if len(sys.argv) == 2:
    arg1 = sys.argv[1]
else:
    print("You must give an input file")
    exit()
    
fo = open(arg1, "r+")
print("Name of the input file: %s" % fo.name)
        
# lines_seen = set() # holds lines already seen
# outfile = open(output, "w")
for line in open(fo.name, "r+"):
    l = line.split()
    print(l)
    for i in l:
        if (re.match(r"([a-z]|[A-Z])", i)):
            print(i)
        
