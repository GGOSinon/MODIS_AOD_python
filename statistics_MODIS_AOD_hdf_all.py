'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 

#Open hdf file
NameError: name 'SD' is not defined
conda install -c conda-forge pyhdf=0.9.0
'''
from glob import glob
import numpy as np
from datetime import datetime
import calendar
import os
from pyhdf.SD import SD, SDC
import threading
from queue import Queue
import sys
from sys import argv
#%%
script, L3_perid = argv # Input L3_perid : 'weekly' 'monthly' 'daily' 
if L3_perid == 'daily' or L3_perid == 'weekly' or L3_perid == 'monthly' :
    print(L3_perid, 'processing started')
else :
    print('input daily weekly monthly')
    sys.exit()
#%%
#for checking time
cht_start_time = datetime.now()
def print_working_time():
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    return print('&'*40, '\n working time :', working_time,'\n'+'&'*40)
#%%
#Set lon, lat, resolution
Llon, Rlon = 90, 150
Slat, Nlat = 10, 60
resolution = 0.05
save_dir_name = '../DAAC_MOD04_3K/{0:03}_{1:03}_{2:2d}_{3:2d}_{4:.2f}_{5}/'\
    .format(Llon, Rlon, Slat, Nlat, resolution, L3_perid)
if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)
    print ('*'*80)
    print (save_dir_name, 'is created')
else :
    print ('*'*80)
    print (save_dir_name, 'is exist')
#%%
#JulianDate_to_date(2018, 131) -- '20180511'
def JulianDate_to_date(y, jd):
    month = 1
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month += 1
    #return datetime(y, month, jd).strftime('%Y%m%d')
    return datetime(y, month, jd)

#date_to_JulianDate('20180201', '%Y%m%d') -- 2018032
def date_to_JulianDate(dt, fmt):
    dt = datetime.strptime(dt, fmt)
    tt = dt.timetuple()
    return int('%d%03d' % (tt.tm_year, tt.tm_yday))

#for modis hdf file, filename = '../DAAC_MOD04_3K/H28V05/MOD04_3K.A2014003.0105.006.2015072123557.hdf'
def filename_to_datetime(filename):
    fileinfo = filename.split('.')
    #print('fileinfo', fileinfo)
    return JulianDate_to_date(int(fileinfo[-5][1:5]), int(fileinfo[-5][5:8]))

def f(proc_date, resolution, Llon, Rlon, Slat, Nlat):
    proc_start_date = proc_date[0]
    proc_end_date = proc_date[1]
    thread_number = proc_date[2]
    write_log = '#This file is created using python \n' \
                '#https://github.com/guitar79/MODIS_AOD \n' \
                + '#start date = ' + str(proc_date[0]) +'\n'\
                + '#end date = ' + str(proc_date[1]) +'\n'
    #variables for downloading 
    start_date = datetime(int(proc_start_date[:4]), int(proc_start_date[4:6]), int(proc_start_date[6:8])) #convert startdate to date type
    end_date = datetime(int(proc_end_date[:4]), int(proc_end_date[4:6]), int(proc_end_date[6:8])) #convert startdate to date type
    if not os.path.exists('{0}AOD_3K_{1}_{2}_{3:03}_{4:03}_{5:2d}_{6:2d}_{7:.2f}.npy'\
                          .format(save_dir_name, proc_start_date, proc_end_date, Llon, Rlon, Slat, Nlat, resolution)) \
        or not os.path.exists('{0}AOD_3K_{1}_{2}_{3:03}_{4:03}_{5:2d}_{6:2d}_{7:.2f}_info.txt'\
                          .format(save_dir_name, proc_start_date, proc_end_date, Llon, Rlon, Slat, Nlat, resolution)) :
    
        write_log += '#Llon =' + str(Llon) + '\n' \
                    + '#Rlon =' + str(Rlon) + '\n' \
                    + '#Slat =' + str(Slat) + '\n' \
                    + '#Nlat =' + str(Nlat) + '\n' \
                    + '#resolution =' + str(resolution) + '\n' 
        
        print(proc_start_date, '-', proc_end_date, 'Start making grid arrays...\n', '='*80)
        ni = np.int((Rlon-Llon)/resolution+1.00)
        nj = np.int((Nlat-Slat)/resolution+1.00)
        lon_array = []
        lat_array = []
        data_array = []   
        mean_array = [] 
        cnt_array = [] 
        for i in range(ni):
            lon_line = []
            lat_line = []
            data_line = []
            mean_line = [] 
            cnt_line = [] 
            for j in range(nj):
                lon_line.append(Llon+resolution*i)
                lat_line.append(Nlat-resolution*j)
                data_line.append([])
                mean_line.append([])
                cnt_line.append([])
            lon_array.append(lon_line)
            lat_array.append(lat_line)
            data_array.append(data_line)
            mean_array.append(mean_line)
            cnt_array.append(cnt_line)
        lat_array = np.array(lat_array)
        lon_array = np.array(lon_array)
        print('Grid array is created\n', '='*80)
        print_working_time()
        
        total_data_cnt = 0
        file_no=0
        write_log += '#processing file list\n' + 'No, filename, data \n'
        
        for k in sorted(glob(os.path.join(dir_name, '*.hdf'))):
            result_array = data_array
            file_date = filename_to_datetime(k)
            #print('fileinfo', file_date)
            
            if file_date >= start_date \
                and file_date < end_date : 
                                
                try:
                    hdf = SD(k, SDC.READ)
                    # Read AOD dataset.
                    DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
                    hdf_raw = hdf.select(DATAFIELD_NAME)
                    aod_data = hdf_raw[:,:]
                    scale_factor = hdf_raw.attributes()['scale_factor']
                    add_offset = hdf_raw.attributes()['add_offset']
                    aod = aod_data * scale_factor + add_offset
                    aod[aod < 0] = np.nan
                    aod = np.asarray(aod)
                
                    # Read geolocation dataset.
                    lat = hdf.select('Latitude')
                    latitude = lat[:,:]
                    lon = hdf.select('Longitude')
                    longitude = lon[:,:]
                except:
                    print("Something got wrecked \n", '='*80)
                    continue
                            
                if np.shape(longitude) != np.shape(latitude) or np.shape(latitude) != np.shape(aod) :
                    print('data shape is different!! \n', '='*80)
                else : 
                    lon_cood = np.array(((longitude-Llon)/resolution*100//100), dtype=np.uint16)
                    lat_cood = np.array(((Nlat-latitude)/resolution*100//100), dtype=np.uint16)
                    data_cnt = 0
                    for i in range(np.shape(lon_cood)[0]) :
                        for j in range(np.shape(lon_cood)[1]) :
                            if int(lon_cood[i][j]) < np.shape(lon_array)[0] \
                                and int(lat_cood[i][j]) < np.shape(lon_array)[1] \
                                and not np.isnan(aod[i][j]) :
                                data_cnt += 1 #for debug
                                result_array[int(lon_cood[i][j])][int(lat_cood[i][j])].append(aod[i][j])
                    file_no += 1
                    total_data_cnt += data_cnt
                write_log += str(file_no) + ',' + str(data_cnt) +',' + str(k) + '\n'
                print(L3_perid, thread_number,  proc_date[0], 'number of files: ', file_no, 'tatal data cnt :' , data_cnt)
        write_log += '#total data number =' + str(total_data_cnt) + '\n'
        
        print(proc_start_date, '-', proc_end_date, 'Calculating mean value at each pixel is being started\n', '='*80)
        print_working_time()
        
        cnt2 = 0 #for debug
        for i in range(np.shape(result_array)[0]):
            for j in range(np.shape(result_array)[1]):
                cnt2 += 1 #for debug
                if len(result_array[i][j])>0: mean_array[i][j] = np.mean(result_array[i][j])
                else : mean_array[i][j] = np.nan
                cnt_array[i][j] = len(result_array[i][j])
        print(thread_number, 'cnt2 :' , cnt2)
        
        mean_array = np.array(mean_array)
        cnt_array = np.array(cnt_array)    
        save_array = np.array([lon_array, lat_array, mean_array])
        np.save('{0}AOD_3K_{1}_{2}_{3:03}_{4:03}_{5:2d}_{6:2d}_{7:.2f}.npy'\
                .format(save_dir_name, proc_start_date, proc_end_date, Llon, Rlon, Slat, Nlat, resolution), save_array)
        print('{0}AOD_3K_{1}_{2}_{3:03}_{4:03}_{5:2d}_{6:2d}_{7:.2f}.npy is creaated\n'\
              .format(save_dir_name, proc_start_date, proc_end_date, Llon, Rlon, Slat, Nlat, resolution), '#'*80)
        with open('{0}AOD_3K_{1}_{2}_{3:03}_{4:03}_{5:2d}_{6:2d}_{7:.2f}_info.txt'\
                .format(save_dir_name, proc_start_date, proc_end_date, Llon, Rlon, Slat, Nlat, resolution), 'w') as f:
            f.write(write_log)
        return mean_array, cnt_array
    else : 
        print('{0}AOD_3K_{1}_{2}_{3:03}_{4:03}_{5:2d}_{6:2d}_{7:.2f}.npy is exist\n'\
              .format(save_dir_name, proc_start_date, proc_end_date, Llon, Rlon, Slat, Nlat, resolution), '$'*80)
        return 

    print('Thread '+str(thread_number)+' finished')
    print_working_time()
#%%
years = range(2000, 2019)
for year in years :
    dir_name = '../DAAC_MOD04_3K/' + str(year) + '/'
    print_lock = threading.Lock()
    def process_queue():
        while True:
            file_data = compress_queue.get()
            f(file_data, resolution, Llon, Rlon, Slat, Nlat)
            compress_queue.task_done()
    compress_queue = Queue()
    
    #%%
    from dateutil.relativedelta import relativedelta
    s_start_date = datetime(year, 1, 1) #convert startdate to date type
    s_end_date = datetime(year, 12, 31)
    
    date_No=0
    date1 = s_start_date
    date2 = s_start_date
    dates = []
    while date2 < s_end_date : 
        date_No += 1
        if L3_perid == 'daily' :
            date2 = date1 + relativedelta(days=1)
        elif L3_perid == 'weekly' :
            date2 = date1 + relativedelta(days=8)
        elif L3_perid == 'monthly' :
            date2 = date1 + relativedelta(months=1)

        date1_strf = date1.strftime('%Y%m%d')
        date2_strf = date2.strftime('%Y%m%d')
        date = (date1_strf, date2_strf, date_No)
        dates.append(date)
        date1 = date2
    
    num_cpu = 14
    
    for i in range(num_cpu):
        t = threading.Thread(target=process_queue)
        t.daemon = True
        t.start()
    
    for date in dates :
        compress_queue.put(date)
    
    compress_queue.join()
