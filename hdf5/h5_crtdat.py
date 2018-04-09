#
# This examaple creates an HDF5 file dset.h5 and an empty datasets /dset in it.
#
import h5py
#
# Create a new file using defaut properties.
#
file = h5py.File('dset.h5','w')
#
# Create a dataset under the Root group.
#
dataset = file.create_dataset("dset",(4, 6), h5py.h5t.STD_I32BE)
print("Dataset dataspace is %s" % str(dataset.shape))
print("Dataset Numpy datatype is %s" % str(dataset.dtype))
print("Dataset name is %s" % str(dataset.name))
print("Dataset is a member of the group %s" % str(dataset.parent))
print("Dataset was created in the file %s" % str(dataset.file))
#
# Close the file before exiting
#
file.close()

