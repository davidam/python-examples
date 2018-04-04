import os, re

num = input("Write a number: ")

print("Is it your number from 1 to 12? ")
match = re.search(r'^(1[0-2]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 24? ")
match = re.search(r'^(2[0-4]|1[0-9]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 31? ")
match = re.search(r'^(3[01]|[12][0-9]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 53? ")
match = re.search(r'^(5[0123]|[1-4][0-9]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 0 to 59? ")
match = re.search(r'^([1-5][0-9]|[0-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 0 to 100? ")
match = re.search(r'^([1]?[0-9]?[0-9])$', num)
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 100? ")
match = re.search(r'^(100|[1-9][0-9]|[1-9])$', num)
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")
    
print("Is it your number from 32 to 126? ")
match = re.search(r'^(12[0-6]|1[0-1][0-9]|[4-9][0-9]|3[2-9])$', num)
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

