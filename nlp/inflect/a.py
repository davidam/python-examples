# Import the libraries
import inflect

# Declare method of inflect module
p = inflect.engine()

print("Did you want " + p.a('thing') + " or " + p.a('idea') + "?")
