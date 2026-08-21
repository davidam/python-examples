# Program to pluralize a given
# word in Python

# Import the libraries
import inflect

# Declare method of inflect module
p = inflect.engine()

print(p.join(("apple", "banana", "carrot")))
print(p.join(("apple", "banana")))
print(p.join(("apple", "banana", "carrot"), final_sep=""))
print(p.join(('apples', 'bananas', 'carrots'), final_sep="", conj='and even'))
print(p.join(('apple', 'banana', 'carrot'), sep='/', sep_spaced=False, conj='', conj_spaced=False))
