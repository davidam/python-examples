import csv
from pprint import pprint
import re

result=""
l1 = []
with open('nombres_por_edad_media_femeninos.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filefem = open('femeninos.txt','w') 
    for row in spamreader:
        l1.append(row[1])
    l1sorted = sorted(l1, key=str.lower)
    for item in l1sorted:
        filefem.write(item+"\n")
    
filefem.close()
        
l2 = []
with open('nombres_por_edad_media_masculinos.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filemasc = open('masculinos.txt','w') 
    for row in spamreader:
        l2.append(row[1])
    l2sorted = sorted(l2, key=str.lower)
    for item in l2sorted:
        filemasc.write(item+"\n")

filemasc.close()


#        print(sorted(l, key=str.lower))
#        print(row[1])
        # if re.search(r"'", row[1]):
        #     result = re.sub(r"'", "", row[1])
        # pprint(result)

