from genderize import Genderize
import csv
import requests
import json

#print(Genderize().get(['James', 'Eva', 'Thunderhorse']))

with open('partial.csv') as csvfile:
    genderapireader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(genderapireader, None)
    genderapilist = []
    for row in genderapireader:
        name = row[0]
        male = row[4]
        name = name.replace('"', '')
        male = male.replace('"', '')
        genderapilist.append((name,male))

print(genderapilist)
