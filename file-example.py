#!/usr/bin/python

# Open a file
fo = open("README.org", "r+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline(1)
print("Read Line: %s" % (line))

# Again set the pointer to the beginning
fo.seek(1)
line = fo.readline()
print("Read Line: %s" % (line))

# Close opend file
fo.close()
