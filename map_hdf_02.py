''' created by Kevin 
 Open hdf file
'''

#import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
#import pyhdf
from pyhdf.SD import SD, SDC

# Open file.
#FILE_NAME = 'AIRS.2002.08.01.L3.RetStd_H031.v4.0.21.0.G06104133732.hdf'
FILE_NAME = '/media/guitar79/8T/RS_data/MODIS/DAAC_MOD04_3K/H28V05/MYD04_3K.A2016366.0440.006.2017010010311.hdf'
hdf = SD(FILE_NAME, SDC.READ)

# List available SDS datasets.
print (hdf.datasets())
#{'Longitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 0), 'Latitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 1), 'Scan_Start_Time': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 6, 2), 'Solar_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 3), 'Solar_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 4), 'Sensor_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 5), 'Sensor_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 6), 'Scattering_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 7), 'Glint_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 8), 'Land_Ocean_Quality_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 9), 'Land_sea_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 10), 'Wind_Speed_Ncep_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 11), 'Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 12), 'Image_Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 13), 'Aerosol_Type_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 14), 'Fitting_Error_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 15), 'Surface_Reflectance_Land': (('Solution_2_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 676, 451), 22, 16), 'Corrected_Optical_Depth_Land': (('Solution_3_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 676, 451), 22, 17), 'Corrected_Optical_Depth_Land_wav2p1': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 18), 'Optical_Depth_Ratio_Small_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 19), 'Number_Pixels_Used_Land': (('Solution_1_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 20), 'Mean_Reflectance_Land': (('MODIS_Band_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 21), 'STD_Reflectance_Land': (('MODIS_Band_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 22), 'Mass_Concentration_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 23), 'Aerosol_Cloud_Fraction_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 24), 'Quality_Assurance_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Land:mod04'), (676, 451, 5), 20, 25), 'Solution_Index_Ocean_Small': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 26), 'Solution_Index_Ocean_Large': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 27), 'Effective_Optical_Depth_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 28), 'Effective_Optical_Depth_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 29), 'Optical_Depth_Small_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 30), 'Optical_Depth_Small_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 31), 'Optical_Depth_Large_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 32), 'Optical_Depth_Large_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 33), 'Mass_Concentration_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 5, 34), 'Aerosol_Cloud_Fraction_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 35), 'Effective_Radius_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 36), 'PSML003_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 5, 37), 'Asymmetry_Factor_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 38), 'Asymmetry_Factor_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 39), 'Backscattering_Ratio_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 40), 'Backscattering_Ratio_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 41), 'Angstrom_Exponent_1_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 42), 'Angstrom_Exponent_2_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 43), 'Least_Squares_Error_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 44), 'Optical_Depth_Ratio_Small_Ocean_0.55micron': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 45), 'Optical_Depth_by_models_ocean': (('Solution_Index:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (9, 676, 451), 22, 46), 'Number_Pixels_Used_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 47), 'Mean_Reflectance_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 48), 'STD_Reflectance_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 49), 'Quality_Assurance_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Ocean:mod04'), (676, 451, 5), 20, 50), 'Topographic_Altitude_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 51)}

DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'

'''
hdfid = hdf_sd_start(file(0))
hdf_sd_readonly,hdfid,'Optical_Depth_Land_And_Ocean',aod
hdf_sd_readonly,hdfid,'Longitude',lon
hdf_sd_readonly,hdfid,'Latitude',lat
scale_factor = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','scale_factor')
offset = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','add_offset')
hdf_sd_end,hdfid
'''

# Read AOD dataset.
data3D = hdf.select(DATAFIELD_NAME)
data = data3D[0,:]
scale_factor = data3D[1,:]
#scale_factor = hdf.select(DATAFIELD_NAME,scale_factor)

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


