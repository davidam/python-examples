import re

m = re.match(r"(\w+) (\w+) (\w+)", "Isaac Newton physicist")
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(1, 2, 3))

n = re.match(r"([[a-z]*]) (\w+) (\w+)", "[asf] tests Hola")
print(n.group(0))
print(n.group(1))
print(n.group(2))

q = re.match(r"([[a-z]*]) (.*)", "[asf] tests Hola")
print(q.group(0))
print(q.group(1))
print(q.group(2))
