import inflect
p = inflect.engine()
print(p.number_to_words(1))
print(p.number_to_words(38))
print(p.number_to_words(1234))
print(p.number_to_words(p.ordinal(1234)))
