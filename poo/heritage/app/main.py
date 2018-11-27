# in method getDescrition we are able to call getName(), getColor() because they are
# accessible to child class through inheritance

from vehicle import Vehicle
from car import Car

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName())
