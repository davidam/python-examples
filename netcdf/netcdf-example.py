# Creating/Opening/Closing a netCDF file

from netCDF4 import Dataset
rootgrp = Dataset("test.nc", "w", format="NETCDF4")
print rootgrp.data_model
rootgrp.close()
