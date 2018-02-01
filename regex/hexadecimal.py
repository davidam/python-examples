import os, re

num = raw_input("Write a hexadecimal number: ")


print("Do you find any hexadecimal number in a larger body of text?: ")
match = re.search(r'\b[0-9A-F]+\b', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Check wheter a text string holds just a hexadecimal number: ")
match = re.search(r'\b[0-9A-F]{6}\b', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")
