#!/usr/bin/python

from random import randint

number = randint(0,100)
guess = int(input("Guess a number: "))

while (guess != number):
    if (guess > number):
        guess = int(input("The number is smaller. Guess a number: ")) 
    elif (guess < number):
        guess = int(input("The number is bigger. Guess a number: ")) 
print("The number is "+ str(guess) + " Congratulations!")
        
