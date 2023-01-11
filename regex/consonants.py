import re

string0 = input('You must write here: ')
m = re.match(r"([bcdfghjklmnñpqrstvwxz])+", string0)
if m:
    print("There are only consonants of the alphabet in the input")
else:
    print("There are not only consonants of the alphabet in the input")
