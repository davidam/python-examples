# Program to pluralize a given
# word in Python

# Import the libraries
import inflect

# Declare method of inflect module
p = inflect.engine()
count = input('You must write an integer: ')

print('There', p.plural_verb('was', count), p.number_to_words(count), p.plural_noun('person', count), 'by the door.')

# count=1
#count = 243

print('There', p.plural_verb('was', count), p.number_to_words(count), p.plural_noun('person', count), 'by the door.')
