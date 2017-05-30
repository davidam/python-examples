def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()

# yield accumulates values to be applied in a for

for i in mygenerator:
    print(i)

    
