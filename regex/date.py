import os, re

f = os.popen('date "+%Y-%m-%d"')
d = f.read()
now = "Today is " + d
print(now)

match = re.search(r'\b(\d\d\d\d)-(\d\d)-(\d\d)\b', now)
# If-statement after search() tests if it succeeded
if match:                      
    print("found") # match.group() ## 'found word:cat'
else:
    print("did not find")
