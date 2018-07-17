import json
from pprint import pprint

jsontext = '{"fruits": ["apple", "banana", "orange"]}'
j = json.loads(jsontext);
print(j['fruits'])

# Open a file
fo = open("db.json", "r+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

jsondata = open('db.json').read()
json_object = json.loads(jsondata)
print(json_object)

with open('db.json') as json_data:
    d = json.load(json_data)
    print(d)
    list1 = d['clients']
    print("################################## list1: ", list1)
    print("################################## element 1: ", list1[0])
    print("################################## element 1 keys: ", list(list1[0].keys()))
    print("################################## element 1 values: ", list(list1[0].values()))    
    # list2 = d['clients'].values()
    # print("list2: ", list2)
    
# Close opend file
fo.close()
