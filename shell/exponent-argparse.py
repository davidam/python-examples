#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-base", type=int,
                    help="display a base number")
parser.add_argument("-exponent", type=int,
                    help="an exponent of a given base")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
# print(args.base)
# print(args.exponent)


result = args.base
for i in range(1, args.exponent):
    result = result * args.base

#print(result)    
if args.verbose:
    print("the base is {}, the exponent is {}, the result is {}".format(args.base, args.exponent, result))
else:
    print(result)
