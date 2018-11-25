'''
Created on Mon Nov  5 18:47:09 2018
@author: guitar79
created by Kevin 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

from glob import glob
import os

years = ['2015', '2016', '2017']

for year in years :
    dir_name = 'DAAC_MOD04_3K/'+year+'/'
    save_dir_name = 'DAAC_MOD04_3K/duplicate/'+year+'/'
    if not os.path.exists(save_dir_name):
        os.makedirs(save_dir_name)
        print ('*'*80)
        print (save_dir_name, 'is created')
    else :
        print ('*'*80)
        print (save_dir_name, 'is exist')
    
    p_fullname = 'a.a'
    #f_name = 'MYD04_3K.A2016366.0440.006.2017010010311.hdf'
    for fullname in sorted(glob(os.path.join(dir_name, '*.hdf')), reverse=True):
        try:
            p_filename = p_fullname.split('/')
            p_filename_el = p_filename[-1].split('.')
            filename = fullname.split('/')
            c_filename_el = filename[-1].split('.')
            
            if p_filename_el[0] == c_filename_el[0] \
                and p_filename_el[1] == c_filename_el[1] \
                and p_filename_el[2] == c_filename_el[2] :
                os.rename(fullname, save_dir_name+filename[-1])
                print(fullname, 'is moved!!')
            else : 
                p_fullname = fullname
        
        except:
            print("Something got wrecked \n")
            continue
