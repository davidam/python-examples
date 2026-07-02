# Program to pluralize a given
# word in Python

# Import the libraries
import inflect

# Declare method of inflect module
p = inflect.engine()

# Define the string and store it in variable
a = 'child'
b = 'apple'
c = 'man'
d = 'woman'

# Print the plural of the string defined
print("Plural of child: ", p.plural(a))
print("Plural of apple: ", p.plural(b))
print("Plural of man: ", p.plural(c))
print("Plural of woman: ", p.plural(d))

