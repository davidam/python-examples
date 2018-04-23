#!/usr/bin/python

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

li = ["a", "b", "mpilgrim", "z", "example"]
li[0]  
li.extend(["two", "elements"])
li.insert(2, "new")
li.index("example")
li.remove("example")

lista = ['a', 'b', 'mpilgrim']
lista = lista + ['example', 'new']
lista += ['two']

# prints out 1,2,3
for x in li:
    print(x)

milista = ['This', 'used', 'to', 'be', 'a', 'Whopping', 'Great', 'sentence']
print(sorted(milista, key=str.lower))

