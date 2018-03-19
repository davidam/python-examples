#!/usr/bin/python# -*- coding: utf-8 -*-

def x(a,b):
    print("param 1 %s param 2 %s" % (a,b))

def y(z,t):
    z(*t)   # z is the function and t are the args
    
y(x,("hello","manuel"))
