from netCDF4 import Dataset
rootgrp = Dataset("test.nc", "a")
fcstgrp = rootgrp.createGroup("forecasts")
analgrp = rootgrp.createGroup("analyses")
print(rootgrp.groups)

def walktree(top):
    values = top.groups.values()
    yield values
    for value in top.groups.values():
        for children in walktree(value):
            yield children

print(rootgrp)

for children in walktree(rootgrp):
     for child in children:
         print(child)
