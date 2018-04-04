#!/usr/bin/python

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

month = 13
days = 32

print('Give me days in a month')
for i in range(1, days):
    if (i < 10):
        print("0"+str(i))
    else:
        print(i)

print('Give me months in a year')    
for i in range(1, month):
    if (i < 10):    
        print("0"+str(i))
    else:
        print(i)
