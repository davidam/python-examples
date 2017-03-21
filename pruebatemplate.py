from string import Template

plantilla = Template("La ciudad de $ciudad aporta $$$cantidad al proyecto ${proyecto}landia.")
ciudad1 = plantilla.substitute(ciudad="New York", proyecto="Cepi", cantidad="150000")
ciudad2 = plantilla.substitute(cantidad="157000", ciudad="Boston", proyecto="Python")
print(ciudad1)
print(ciudad2)
