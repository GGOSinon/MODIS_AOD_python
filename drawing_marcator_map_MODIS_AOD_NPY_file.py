#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
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
#%%
from glob import glob
import numpy as np
from datetime import datetime
import locale
import os
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys
from sys import argv
script, L3_perid = argv # Input L3_perid : 'weekly' 'monthly' 'daily' 
#%%
#L3_perid = 'weekly' # 'monthly' 'daily' 'weekly'
if L3_perid == 'daily' or L3_perid == 'weekly' or L3_perid == 'monthly' :
    print(L3_perid, 'processing started')
else :
    print('input daily weekly monthly')
    sys.exit()
    
dir_name = '../DAAC_MOD04_3K/090_150_10_60_0.05_{0}/'.format(L3_perid)
save_dir_name = '../DAAC_MOD04_3K/090_150_10_60_0.10_{0}_cyl/'.format(L3_perid)
#%%
#for checking time
cht_start_time = datetime.now()
def print_working_time():
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    return print('&'*40, '\n working time :', working_time,'\n'+'&'*40)

#%%
#for modis hdf file, filename = 'DAAC_MOD04_3K/daily/AOD_3K_20150101_20150102_90_150_10_60_0.1.npy'
def npy_filename_to_fileinfo(filename):
    fileinfo = filename.split('_')
    start_date = fileinfo[-7]
    end_date = fileinfo[-6]
    resolution = fileinfo[-1][0:3]
    return start_date, end_date, resolution

#%%    
#f_name = dir_name+'AOD_3K_20161229_20170106_90_150_10_60_0.1.npy'
for f_name in sorted(glob(os.path.join(dir_name, '*.npy'))):
    if not os.path.exists(f_name[:-4]+'_cyl.png'):
        try :
            locale.setlocale(locale.LC_ALL, "C.UTF-8")
            start_date, end_date, resolution = npy_filename_to_fileinfo(f_name)
            
            startdate = datetime(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
            startdate = startdate.strftime("%d, %b, %Y")
            enddate = datetime(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
            enddate = enddate - relativedelta(days=1)
            enddate = enddate.strftime("%d, %b, %Y")
            
            hdf_data = np.load(f_name)
            lon_array = hdf_data[0,:,:]
            lat_array = hdf_data[1,:,:]
            aod = hdf_data[2,:,:]
            aod_max = np.nanmax(aod)
            aod_mean = np.nanmean(aod)
            
            Llon = np.min(hdf_data[0,:,:])
            Rlon = np.max(hdf_data[0,:,:])
            Slat = np.min(hdf_data[1,:,:])
            Nlat = np.max(hdf_data[1,:,:])
            
            #Plot data on the map
            print('='*80)
            print(startdate, '::: Plotting data on the map......\n', f_name)
            fig = plt.figure(figsize=(10, 10))
            fig.suptitle('Aerosol optical depth (MODIS: Terra, Aqua)', fontsize=20)
            
            ax = fig.add_subplot(111)
            fig.subplots_adjust(top=1.05)
            
            if L3_perid=='daily' :
                ttitle = '      (' + startdate + ')\n'
            elif L3_perid=='weekly' or L3_perid=='monthly' :
                ttitle = '    (' + startdate + ' - ' + enddate + ')\n'
            else : 
                L3_perid = ''
            
            ax.set_title(ttitle, fontsize=14)
            
            # sylender map
            ax = Basemap(projection='cyl', resolution='h', \
                        llcrnrlat = Slat, urcrnrlat = Nlat, \
                        llcrnrlon = Llon, urcrnrlon = Rlon)
            ax.drawcoastlines(linewidth=0.25)
            ax.drawcountries(linewidth=0.25)
            
            ax.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0])
            ax.drawmeridians(np.arange(-180., 181., 15.), labels=[0, 0, 0, 1])
            
            x, y = ax(lon_array, lat_array) # convert to projection map
            
            vvmax=5
            im = plt.pcolormesh(x, y, aod, vmin=0, vmax=vvmax)
            plt.colorbar(cmap='bwr', fraction=0.0383, pad=0.04, ticks=(np.arange(0, vvmax+0.1, step=0.5)))

            x1,y1 = ax(150, 59.7)
            plt.text(x1, y1, 'Maximun value: {0:.5f}\nMean value: {1:.5f}\n'\
                     .format(aod_max, aod_mean), 
                     horizontalalignment='right',
                     verticalalignment='bottom', 
                     fontsize=9, style='italic', wrap=True)
            x2,y2 = ax(150, 7)
            plt.text(x2, y2, 'created by guitar79@gs.hs.kr\n\
                     The NASA Level-1 and Atmosphere Archive & Distribution System (LAADS)\n \
                     Distributed Active Archive Center (DAAC), Goddard Space Flight Center, Greenbelt, MD.'
                     .format(aod_max, aod_mean), 
                     horizontalalignment='right',
                     verticalalignment='top', 
                     fontsize=12, style='italic', wrap=True)
            
            plt.savefig(f_name[:-4]+'_cyl.png', bbox_inches='tight', dpi = 300)
            #plt.savefig(f_name[:-4]+'.pdf', bbox_inches='tight', dpi = 300)
            print('='*80)
            print(f_name[:-4]+'.png is created', L3_perid)
            #plt.show()
            print_working_time()
            
        except Exception as err:
            print('Something got wrecked', L3_perid)
            print(err)
            print_working_time()
            continue