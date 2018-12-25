#! /usr/bin/env python
# created by Kevin 
# Open hdf file

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from pyhdf.SD import SD, SDC

# Open file.
#FILE_NAME = 'AIRS.2002.08.01.L3.RetStd_H031.v4.0.21.0.G06104133732.hdf'
FILE_NAME = '/media/guitar79/8T/RS_data/MODIS/DAAC_MOD04_3K/H28V05/MYD04_3K.A2016366.0440.006.2017010010311.hdf'
hdf = SD(FILE_NAME, SDC.READ)

# List available SDS datasets.
#print hdf.datasets()

# Read dataset.

##### FILE_NAME = '/media/guitar79/8T/RS_data/FromDAAC/Aerosol_10km/H28V05/MOD04_L2.A2016001.0020.006.2016008004525.hdf'
##### 'Optical_Depth_Small_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 32), 
##### 'Asymmetry_Factor_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 39), 
##### 'Aerosol_Cloud_Fraction_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 36), 'Deep_Blue_Angstrom_Exponent_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 54), 
##### 'Angstrom_Exponent_2_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 44), 'Effective_Optical_Depth_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 29), 
##### 'Mean_Reflectance_Ocean': (('MODIS_Band_AND_NPP_Extra:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (10, 203, 135), 22, 49), 
##### 'Optical_Depth_Small_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 31), 'Wind_Speed_Ncep_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 69), 
##### 'STD_Reflectance_Land': (('MODIS_Band_AND_NPP_Extra:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (10, 203, 135), 22, 23), 
##### 'Solar_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 3), 
##### 'STD_Reflectance_Ocean': (('MODIS_Band_AND_NPP_Extra:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (10, 203, 135), 22, 50), 
##### 'Effective_Radius_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 203, 135), 22, 37), 
##### 'Latitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 5, 1), 
##### 'Sensor_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 6), 
##### 'Quality_Assurance_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Ocean:mod04'), (203, 135, 5), 20, 51), 
##### 'Surface_Reflectance_Land': (('Solution_2_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 203, 135), 22, 17), 
##### 'Glint_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 68), 
##### 'Sensor_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 5), 
##### 'Scan_Start_Time': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 6, 2), 
##### 'Image_Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 13), 
##### 'Effective_Optical_Depth_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 30), 
##### 'Deep_Blue_Spectral_TOA_Reflectance_Land': (('Num_DeepBlue_Wavelengths:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 203, 135), 22, 57), 
##### 'Optical_Depth_Large_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 34), 
##### 'Mass_Concentration_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 5, 24), 
##### 'Aerosol_Cldmask_Land_Ocean': (('Cell_Along_Swath_500:mod04', 'Cell_Across_Swath_500:mod04'), (4060, 2708), 22, 9), 
##### 'Average_Cloud_Pixel_Distance_Land_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 14), 
##### 'Topographic_Altitude_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 70), 
##### 'Deep_Blue_Spectral_Surface_Reflectance_Land': (('Num_DeepBlue_Wavelengths:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 203, 135), 22, 56), 
##### 'Optical_Depth_Large_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 33), 
##### 'Corrected_Optical_Depth_Land_wav2p1': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 19), 
##### 'PSML003_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 203, 135), 5, 38), 
##### 'AOD_550_Dark_Target_Deep_Blue_Combined_Algorithm_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 67), 
##### 'Backscattering_Ratio_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 42), 
##### 'Cloud_Pixel_Distance_Land_Ocean': (('Cell_Along_Swath_500:mod04', 'Cell_Across_Swath_500:mod04'), (4060, 2708), 22, 10), 
##### 'Solution_Index_Ocean_Small': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 203, 135), 22, 27), 
##### 'Deep_Blue_Cloud_Fraction_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 60), 'AOD_550_Dark_Target_Deep_Blue_Combined': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 65), 
##### 'Land_sea_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 8), 
##### 'Longitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 5, 0), 
##### 'Aerosol_Type_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 15), 
##### 'Effective_Optical_Depth_0p55um_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 71), 
##### 'Deep_Blue_Aerosol_Optical_Depth_550_Land_Estimated_Uncertainty': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 64), 
##### 'Backscattering_Ratio_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 41), 
##### 'Aerosol_Cloud_Fraction_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 25), 
##### 'Corrected_Optical_Depth_Land': (('Solution_3_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 203, 135), 22, 18), 
##### 'Least_Squares_Error_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 203, 135), 22, 45), 
##### 'Optical_Depth_Ratio_Small_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 20), 
##### 'Scattering_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 7), 
##### 'Angstrom_Exponent_1_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 43), 
##### 'Optical_Depth_Ratio_Small_Ocean_0.55micron': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 46), 
##### 'AOD_550_Dark_Target_Deep_Blue_Combined_QA_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 66), 
##### 'Mass_Concentration_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 203, 135), 5, 35), 
##### 'Mean_Reflectance_Land': (('MODIS_Band_AND_NPP_Extra:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (10, 203, 135), 22, 22), 
##### 'Asymmetry_Factor_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 203, 135), 22, 40), 
##### 'Solar_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 4), 
##### 'Quality_Assurance_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Land:mod04'), (203, 135, 6), 20, 26), 
##### 'Land_Ocean_Quality_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 11), 
##### 'Deep_Blue_Aerosol_Optical_Depth_550_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 52), 
##### 'Deep_Blue_Aerosol_Optical_Depth_550_Land_Best_Estimate': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 63), 
##### 'Fitting_Error_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 16), 
##### 'Deep_Blue_Algorithm_Flag_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 62), 
##### 'Deep_Blue_Spectral_Aerosol_Optical_Depth_Land': (('Num_DeepBlue_Wavelengths:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 203, 135), 22, 53), 
##### 'Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 12),
#####  'Number_Pixels_Used_Ocean': (('MODIS_Band_AND_NPP_Extra:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (10, 203, 135), 22, 48), 
##### 'Deep_Blue_Aerosol_Optical_Depth_550_Land_STD': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 59), 
##### 'Deep_Blue_Aerosol_Optical_Depth_550_Land_QA_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 61), 
##### 'Solution_Index_Ocean_Large': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 203, 135), 22, 28), 
##### 'Number_Pixels_Used_Land': (('MODIS_Band_AND_NPP_Extra:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (10, 203, 135), 22, 21), 
##### 'Deep_Blue_Spectral_Single_Scattering_Albedo_Land': (('Num_DeepBlue_Wavelengths:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 203, 135), 22, 55), 
##### 'Optical_Depth_by_models_ocean': (('Solution_Index:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (9, 203, 135), 22, 47), 
##### 'Deep_Blue_Number_Pixels_Used_550_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (203, 135), 22, 58)}




#DATAFIELD_NAME='RelHumid_A'
#DATAFIELD_NAME='Optical_Depth_Land_and_Ocean'
DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'

#hdfid = hdf_sd_start(file(0))
	#hdf_sd_readonly,hdfid,'Optical_Depth_Land_And_Ocean',aod
	#hdf_sd_readonly,hdfid,'Longitude',lon
	#hdf_sd_readonly,hdfid,'Latitude',lat
	
	#scale_factor = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','scale_factor')
	#offset = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','add_offset')
	#hdf_sd_end,hdfid

data3D = hdf.select(DATAFIELD_NAME)
data = data3D[0,:,:]  # error

# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]

m = Basemap(projection='cyl', resolution='l', llcrnrlat=10, urcrnrlat = 60, llcrnrlon=100, urcrnrlon = 160)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
x, y = m(longitude, latitude)
m.pcolormesh(x, y, data)





##from pyhdf.SD import *
### import Numeric Python package -- Numpy
##from numpy import *
##
##data = array(((1, 2, 3),
##(4, 5, 6)), int16)
##
### Create an HDF file
##sd = SD("hello.hdf", SDC.WRITE | SDC.CREATE)
##
### Create a dataset
##sds = sd.create("sds1", SDC.INT16, (2, 3))
##
### Fill the dataset with a fill value
##sds.setfillvalue(0)
##
### Set dimension names
##dim1 = sds.dim(0)
##dim1.setname("row")
##dim2 = sds.dim(1)
##dim2.setname("col")
##
### Assign an attribute to the dataset
##sds.units = "miles"
##
### Write data
##sds[:] = data
##
### Close the dataset
##sds.endaccess()
##
### Flush and close the HDF file
##sd.end() 


