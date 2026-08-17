import inflect
engine = inflect.engine()
plural = engine.plural("man")
print(plural)
plural = engine.plural("child")
print(plural)
plural = engine.plural("house")
print(plural)
