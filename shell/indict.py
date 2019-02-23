import os
import re

def in_dict(name):
    f = os.popen('dict '+name)
    in_dict = False
    for line in f:
        if (re.match(r'[0-9]+ definitions found', line)):
            in_dict = True
    return in_dict

print(in_dict("Mesa"))
print(in_dict("Table"))
