import json
from pprint import pprint
jsontext = '{"fruits": ["apple", "banana", "orange"]}'
j = json.loads(jsontext);
print(j['fruits'])
