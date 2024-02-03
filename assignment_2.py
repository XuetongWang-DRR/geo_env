import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
import os

folder_path = '/mnt/datawaha/hyex/wangx0o/research/Course/ErSE394/assignment_2'
# Create the folder if it does not exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)



#Reading the data
dset = xr.open_dataset('/mnt/datawaha/hyex/wangx0o/research/Course/ErSE394/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')
pdb.set_trace()

#Check names of the variables
print(dset.variables.keys())
pdb.set_trace()

#Access the air temperature variable
print(dset['tas'])
pdb.set_trace()

#Check the data type of the air temperature variable
print(dset['tas'].dtype)
pdb.set_trace()


#Check the mean air temperature map for pre industrial period
dset_pre_ind = xr.open_dataset('/mnt/datawaha/hyex/wangx0o/research/Course/ErSE394/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc')
mean_pre_ind = np.mean(dset_pre_ind['tas'].sel(time = slice('18500101', '19001231')), axis = 0)
pdb.set_trace()

#Calculate mean temperature maps for 2071-2100 for each climate scenario:
#ssp119
dset_ssp119 = xr.open_dataset('/mnt/datawaha/hyex/wangx0o/research/Course/ErSE394/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc')
mean_ssp119 = np.mean(dset_ssp119['tas'].sel(time = slice('20710101', '21001231')), axis = 0)
#ssp245
dset_ssp245 = xr.open_dataset('/mnt/datawaha/hyex/wangx0o/research/Course/ErSE394/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc')
mean_ssp245 = np.mean(dset_ssp245['tas'].sel(time = slice('20710101', '21001231')), axis = 0)
#ssp585
dset_ssp585 = xr.open_dataset('/mnt/datawaha/hyex/wangx0o/research/Course/ErSE394/Course_Data/Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc')
mean_ssp585 = np.mean(dset_ssp585['tas'].sel(time = slice('20710101', '21001231')), axis = 0)
pdb.set_trace()


#Calculate the temperature difference between 2071-2100 and 1850-1900 for each climate scenario
temp_diff_ssp119 = mean_ssp119 - mean_pre_ind
temp_diff_ssp245 = mean_ssp245 - mean_pre_ind
temp_diff_ssp585 = mean_ssp585 - mean_pre_ind

#Visualization of temperature differencew
def plot_temp_difference(temp_diff, scenario_name, folder_path):
    plt.figure(figsize=(10, 6))
    plt.imshow(temp_diff, cmap='coolwarm', interpolation='nearest')
    im = plt.imshow(temp_diff, cmap='coolwarm', interpolation='nearest', vmin=-5, vmax=10)
    plt.colorbar(im, label='Temperature Difference (K)')
    plt.title(f'Temperature Difference 2071-2100 vs. 1850-1900: {scenario_name}')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.xticks(np.linspace(0, temp_diff.shape[1], num=5), np.linspace(0, 360, num=5))
    plt.yticks(np.linspace(0, temp_diff.shape[0], num=5), np.linspace(90, -90, num=5))
    # Save the figure in the specified folder
    plt.savefig(os.path.join(folder_path, f'temp_diff_{scenario_name}.png'), dpi=300)
    plt.show()

plot_temp_difference(temp_diff_ssp119, 'SSP1-1.9', folder_path)
plot_temp_difference(temp_diff_ssp245, 'SSP2-4.5', folder_path)
plot_temp_difference(temp_diff_ssp585, 'SSP5-8.5', folder_path)
pdb.set_trace()










