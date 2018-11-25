'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 

#basemap
conda install -c conda-forge basemap-data-hires
conda install -c conda-forge basemap
'''

from glob import glob
import numpy as np
from datetime import datetime
import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#for checking time
cht_start_time = datetime.now()

dir_name = 'DAAC_MOD04_3K/weekly/'

#for modis hdf file, filename = 'DAAC_MOD04_3K/daily/AOD_3K_20150101_20150102_90_150_10_60_0.1.npy'
def npy_filename_to_fileinfo(filename):
    fileinfo = filename.split('_')
    start_date = fileinfo[-7]
    end_date = fileinfo[-6]
    resolution = fileinfo[-1][0:3]
    return start_date, end_date, resolution
    
#f_name = 'AOD_3K_20150101_20150109_90_150_10_60_0.1.npy'
#f_name = dir_name+'AOD_3K_20150101_20150109_90_150_10_60_0.1.npy'
for f_name in sorted(glob(os.path.join(dir_name, '*.npy'))):
    try : 
        start_date, end_date, resolution = npy_filename_to_fileinfo(f_name)
        
        startdate = datetime(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
        startdate = startdate.strftime("%d, %b, %Y")
        enddate = datetime(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
        enddate = enddate.strftime("%d, %b, %Y")
        
        hdf_data = np.load(f_name)
        lon_array = hdf_data[0,:,:]
        lat_array = hdf_data[1,:,:]
        aod = hdf_data[2,:,:]
        Llon = np.min(hdf_data[0,:,:])
        Rlon = np.max(hdf_data[0,:,:])
        Slat = np.min(hdf_data[1,:,:])
        Nlat = np.max(hdf_data[1,:,:])
        
        #Plot data on the map
        print('='*80)
        print('Plotting data on the map......\n', f_name)
        fig = plt.figure(figsize=(10, 10))
        fig.suptitle('MODIS AOD', fontsize=20)
        
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=1.05)
        ax.set_title('     (' + startdate + '  -  '+ enddate+')\n', fontsize=14)
        
        # sylender map
        ax = Basemap(projection='cyl', resolution='h', \
                    llcrnrlat = Slat, urcrnrlat = Nlat, \
                    llcrnrlon = Llon, urcrnrlon = Rlon)
        ax.drawcoastlines(linewidth=0.25)
        ax.drawcountries(linewidth=0.25)
        
        ax.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0])
        ax.drawmeridians(np.arange(-180., 181., 15.), labels=[0, 0, 0, 1])
        
        x, y = ax(lon_array, lat_array) # convert to projection map
        
        plt.pcolormesh(x, y, aod)
        plt.colorbar(cmap='rainbow', fraction=0.038, pad=0.04, ticks=(np.arange(0, 6.1, step=0.25)))
        plt.text(155, 5, 'created by guitar79@gs.hs.kr', fontsize=12, style='italic', ha='right', wrap=True)
        plt.text(155, 2, 'The NASA Level-1 and Atmosphere Archive & Distribution System (LAADS) \n Distributed Active Archive Center (DAAC), Goddard Space Flight Center, Greenbelt, MD.', \
                 fontsize=10, style='italic', ha='right', wrap=True)
        
        plt.savefig(f_name[:-4]+'.png', bbox_inches='tight', dpi = 300)
        plt.savefig(f_name[:-4]+'.pdf', bbox_inches='tight', dpi = 300)
        
        print('='*80)
        print(f_name[:-4]+'.pdf is created')
        #plt.show()
        
    except:
        print("Something got wrecked \n")
        continue