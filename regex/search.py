import re
str = 'an example word:cat!!'
reg = 'word:\w\w\w'
match = re.search(reg, str)
# If-statement after search() tests if it succeeded
if match:                      
    print('found %s' % match.group()) ## 'found word:cat'
else:
    print('did not find')

