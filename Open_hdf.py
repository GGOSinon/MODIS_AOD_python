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
FILE_NAME = '/media/guitar79/8T/RS_data/FromDAAC/Aerosol_10km/H28V05/MOD04_L2.A2016001.0020.006.2016008004525.hdf'
hdf = SD(FILE_NAME, SDC.READ)

# List available SDS datasets.
print hdf.datasets()

# Read dataset.
#DATAFIELD_NAME='RelHumid_A'
DATAFIELD_NAME='Optical_Depth_land_and_Ocean'
data3D = hdf.select(DATAFIELD_NAME)
data = data3D[11,:,:]

# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]

m = Basemap(projection='cyl', resolution='l', llcrnrlat=-90, urcrnrlat = 90, llcrnrlon=-180, urcrnrlon = 180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
x, y = m(longitude, latitude)
m.pcolormesh(x, y, data)


from pyhdf.SD import *
# import Numeric Python package -- Numpy
from numpy import *

data = array(((1, 2, 3),
(4, 5, 6)), int16)

# Create an HDF file
sd = SD("hello.hdf", SDC.WRITE | SDC.CREATE)

# Create a dataset
sds = sd.create("sds1", SDC.INT16, (2, 3))

# Fill the dataset with a fill value
sds.setfillvalue(0)

# Set dimension names
dim1 = sds.dim(0)
dim1.setname("row")
dim2 = sds.dim(1)
dim2.setname("col")

# Assign an attribute to the dataset
sds.units = "miles"

# Write data
sds[:] = data

# Close the dataset
sds.endaccess()

# Flush and close the HDF file
sd.end() 
