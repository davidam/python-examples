import json

with open('data3.json') as json_data:
    d = json.load(json_data)
#    print(d)
    for z in d:
        print(z)
