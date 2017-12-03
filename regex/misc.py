import re

print(not re.match("a", "cat"))
print(re.search("a", "cat"))
print(not re.search("c", "dog"))
print(3 == len(re.split("[ab]", "carbs")))
print("R-D-" == re.sub("[0-9]", "-", "R2D2"))

