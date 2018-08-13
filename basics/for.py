#!/usr/bin/python

words = ['cat', 'window', 'defenestrate']

print("######################## First for: #######################")
for w in words:
    print(w, len(w))

print("######################## Second for: #####################")

for i,w in enumerate(words):
    print(i, w)

print("######################## Third for: #####################")

for i in range(1,10):
    print(i)

print("######################## Fourth for: #####################")

print(','.join('{}'.format(i) for i in range(1, 100, 4)))

print("######################## Fifth for: #####################")

print(','.join('{},{}'.format(i, i + 1) for i in range(1, 100, 4)))
