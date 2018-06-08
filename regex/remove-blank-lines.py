#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re

output = "noblank"

if len(sys.argv) == 2:
    arg1 = sys.argv[1]
else:
    print("You must give an input file")
    exit()
    
fo = open(arg1, "r")
print("Name of the input file: %s", fo.name)
print("Name of the output file: %s", output)
        
lines_seen = set() # holds lines already seen
outfile = open(output, "w")

for line in open(fo.name, "r"):
    print(line)
    if not(re.match(r'^\s*$', line)):
        print(line)
        outfile.write(line)
outfile.close()
