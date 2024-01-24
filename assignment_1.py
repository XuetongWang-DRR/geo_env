import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

#Open the dataset
dset = xr.open_dataset('/mnt/datawaha/hyex/wangx0o/research/Course/ErSE394/Course_Data/SRTMGL1_NC.003_Data/N21E039.SRTMGL1_NC.nc')
pdb.set_trace()

#Extract the elevation data
DEM = np.array(dset.variables['SRTMGL1_DEM'])
dset.close()
pdb.set_trace()

#Plot the elevation data
plt.imshow(DEM)
cbar = plt.colorbar()
cbar.set_label('Elevation(m asl)')
plt.savefig('assignment_1.png', dpi = 300)


