#!/usr/bin/python

bebes = input("Give me the number of babies: ")
bebes = int(bebes)

if bebes == 1:
    print("I've eaten " + str(bebes) + " baby.")
else:
    print("I've eaten " + str(bebes) + " babies.")
    
if bebes > 100:
    print("I'm Edelweiss")
