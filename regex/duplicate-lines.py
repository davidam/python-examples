#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

output = "duplicate.out.log"

if len(sys.argv) == 2:
    arg1 = sys.argv[1]
else:
    print("You must give an input file")
    exit()
    
fo = open(arg1, "rw+")
print "Name of the input file: ", fo.name
print "Name of the output file: ", output
        
lines_seen = set() # holds lines already seen
outfile = open(output, "w")
for line in open(fo.name, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
