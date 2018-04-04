#!/usr/bin/python

def cuenta_atras(num):
    if num == 0:
        print("Final de la cuenta")
    else:
        print(num)
        cuenta_atras(num - 1)

cuenta_atras(10)
