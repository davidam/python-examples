#!/usr/bin/python

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't %s", action)
    print("if you put " + str(voltage) + " volts through it.")
    print("-- Lovely plumage, the " + type)
    print("-- It's " + state + " !")

parrot(1000)   
