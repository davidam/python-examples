import inflect
p = inflect.engine()

print(p.singular_noun("they"))
p.gender("feminine")
print(p.singular_noun("they"))
p.gender("masculine")
print(p.singular_noun("they"))
