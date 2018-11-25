#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:47:09 2018

@author: guitar79
"""

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 

#Open hdf file
NameError: name 'SD' is not defined
conda install -c conda-forge pyhdf=0.9.0
#basemap
conda install -c conda-forge basemap-data-hires
conda install -c conda-forge basemap
'''

from glob import glob
import numpy as np
from datetime import datetime
import calendar
import os
from pyhdf.SD import SD, SDC
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cht_start_time=datetime.now()

Llon, Rlon = 90, 150
Slat, Nlat = 10, 60
resolution = 0.1

dir_name = 'DAAC_MOD04_3K/2016/'
save_dir_name = 'DAAC_MOD04_3K/save/'
if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)
    print ('*'*80)
    print (save_dir_name, 'is created')
else :
    print ('*'*80)
    print (save_dir_name, 'is exist')

f_name = 'MYD04_3K.A2016366.0440.006.2017010010311.hdf'

#JulianDate_to_date(2018, 131) -- '20180511'
def JulianDate_to_date(y, jd):
    month = 1
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month += 1
    #return datetime(y, month, jd).strftime('%Y%m%d')
    return datetime(y, month, jd)

#for modis hdf file, filename = 'DAAC_MOD04_3K/2014/MOD04_3K.A2014003.0105.006.2015072123557.hdf'
def filename_to_datetime(filename):
    fileinfo = filename.split('.')
    #print('fileinfo', fileinfo)
    return JulianDate_to_date(int(fileinfo[1][1:5]), int(fileinfo[1][5:8]))

file_date = filename_to_datetime(dir_name+f_name)
file_date = file_date.strftime("%d, %b, %Y")


hdf = SD(dir_name+f_name, SDC.READ)
        
# Read AOD dataset.
DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
hdf_raw = hdf.select(DATAFIELD_NAME)
aod_data = hdf_raw[:,:]
scale_factor = hdf_raw.attributes()['scale_factor']
add_offset = hdf_raw.attributes()['add_offset']
aod = aod_data * scale_factor + add_offset
aod[aod < 0] = np.nan
aod = np.asarray(aod)

aod_max = np.nanmax(aod)
aod_mean = np.nanmean(aod)

# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]

#Plot data on the map
print('='*80)
print('Plotting data on the map......\n', f_name)
fig = plt.figure(figsize=(10, 10))
fig.suptitle('MODIS AOD', fontsize=20)

ax = fig.add_subplot(111)
fig.subplots_adjust(top=1.05)
ax.set_title('     (' + file_date + ')\n', fontsize=14)

# sylender map
ax = Basemap(projection='cyl', resolution='h', \
            llcrnrlat = Slat, urcrnrlat = Nlat, \
            llcrnrlon = Llon, urcrnrlon = Rlon)
ax.drawcoastlines(linewidth=0.25)
ax.drawcountries(linewidth=0.25)

ax.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0])
ax.drawmeridians(np.arange(-180., 181., 15.), labels=[0, 0, 0, 1])

x, y = ax(longitude, latitude) # convert to projection map

plt.pcolormesh(x, y, aod)
plt.colorbar(cmap='bwr', fraction=0.038, pad=0.04, ticks=(np.arange(0, 6.1, step=0.25)))
plt.text(90, 61, f_name, fontsize=8, style='italic', ha='left', wrap=True)
plt.text(150, 62.5, 'Maximun value : '+ (str(format(aod_max, '.3f'))), fontsize=9, style='italic', ha='right', wrap=True)
plt.text(150, 61, 'Mean value : ' + (str(format(aod_mean, '.3f'))), fontsize=9, style='italic', ha='right', wrap=True)

plt.text(155, 5, 'created by guitar79@gs.hs.kr using python', fontsize=12, style='italic', ha='right', wrap=True)
plt.text(155, 2, 'The NASA Level-1 and Atmosphere Archive & Distribution System (LAADS) \n Distributed Active Archive Center (DAAC), Goddard Space Flight Center, Greenbelt, MD.', \
         fontsize=10, style='italic', ha='right', wrap=True)

plt.savefig(save_dir_name+f_name[:-4]+'.png', bbox_inches='tight', dpi = 300)
#plt.savefig(save_dir_name+f_name[:-4]+'.pdf', bbox_inches='tight', dpi = 300)
print('='*80)
print(save_dir_name+f_name[:-4]+'.png is created')

#plt.show()
