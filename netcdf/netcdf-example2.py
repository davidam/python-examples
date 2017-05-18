# Groups in a netCDF file

from netCDF4 import Dataset
rootgrp = Dataset("test.nc", "a")
fcstgrp = rootgrp.createGroup("forecasts")
analgrp = rootgrp.createGroup("analyses")
print rootgrp.groups
