import re
# Open file
f = open('pg1513.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'Romeo and Juliet', f.read())
print strings
