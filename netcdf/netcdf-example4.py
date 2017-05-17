# Dimensions in a netCDF file.

from netCDF4 import Dataset
rootgrp = Dataset("test.nc", "a")
fcstgrp = rootgrp.createGroup("forecasts")
analgrp = rootgrp.createGroup("analyses")

print rootgrp.groups

level = rootgrp.createDimension("level", None)
time = rootgrp.createDimension("time", None)
lat = rootgrp.createDimension("lat", 73)
lon = rootgrp.createDimension("lon", 144)

print rootgrp.dimensions

print len(lon)
print lon.isunlimited()
print time.isunlimited()

for dimobj in rootgrp.dimensions.values():
    print dimobj
