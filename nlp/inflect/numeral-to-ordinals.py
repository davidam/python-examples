# Import the libraries
import inflect

# Declare method of inflect module
p = inflect.engine()

print("It was " + p.ordinal(1))

print("It was " + p.ordinal(2))

print("It was " + p.ordinal(3))

print("It was " + p.ordinal(4))

print("It was " + p.ordinal(5))

print("It was " + p.ordinal(10))

print("It was " + p.ordinal(347))
