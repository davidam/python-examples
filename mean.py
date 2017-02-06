#!/usr/bin/python
numbers = [1, 2, 3, 4, 5]

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean

print calculate_mean(numbers)
