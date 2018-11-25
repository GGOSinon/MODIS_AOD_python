''' created by Kevin 
 Open hdf file
 # 2018.07.22 
 ubuntu 16.04, Anaconda 3
 conda install basemap
 conda install -c conda-forge pyhdf
'''

#import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
#import pyhdf
from pyhdf.SD import SD, SDC
from datetime import datetime
import time

#julianday = '%d%03d' % (datetime.now().timetuple().tm_year, datetime.now().timetuple().tm_yday)

# Open file.
FILE_NAME = '/media/guitar79/6T1/MODIS_AOD/DAAC_MOD04_3K/all/MOD04_3K.A2014001.0115.006.2015072123556.hdf'
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

aod = (aod + offset.data(0))*scale_factor.data(0)
	nan = where(aod le 0. or aod ge 5.,nanc)
	if nanc gt 0 then aod(nan) = !values.f_nan

'''

# Read AOD dataset.
aod_raw = hdf.select(DATAFIELD_NAME)
aod_attri = aod_raw.attributes()
aod_scale_factor = aod_attri['scale_factor']
add_offset = aod_attri['add_offset']
aod = aod_raw.get()

'''
aod[aod == -9999] = nan
for x in range(0, aod.shape[0]):
    for y in range(0, aod.shape[1]):
        if aod[x, y] <= 0:
            aod[x, y] = NaN
            '''
aod = (aod + add_offset)*aod_scale_factor
aod[aod < 0] = np.nan
#####



#scale_factor = hdf.select(DATAFIELD_NAME,scale_factor)

# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]

m = Basemap(projection='cyl', resolution='l', llcrnrlat=10, urcrnrlat = 60, llcrnrlon=100, urcrnrlon = 160)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90, 90., 10.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 180., 15.), labels=[0, 0, 0, 1])
x, y = m(longitude, latitude)
m.pcolormesh(x, y, aod, vmin=0,vmax=2)
plt.title('MODIS AOD')
plt.colorbar(cmap='rainbow', extend='max')

#plt.savefig('current{}.pdf'.format(time), bbox_inches='tight', dpi = 300)
plt.savefig('current{}.png'.format(time), bbox_inches='tight', dpi = 300)


'''
frol IDL code..
PRO MODIS_L2_AOD_READ, file=file, aod=aod, lat=lat, lon=lon

;--modispath	= '/media/guitar79/8T/RS_data/MODIS/DAAC_MOD04_3K/H26V05/'
;--modisname	= 'MOD04_3K.A2015089.0320.006.2015089140334.hdf'
;--file 		= file_search(modispath+modisname, count = modisfilen)

;--if modisfilen lt 1 then begin

;--	print,'====================================='
;--	print,'Cannot find MODIS L2 file:'+modisname
;--	print,'====================================='

;--endif else begin

	hdfid = hdf_sd_start(file(0))
	hdf_sd_readonly,hdfid,'Optical_Depth_Land_And_Ocean',aod
	hdf_sd_readonly,hdfid,'Longitude',lon
	hdf_sd_readonly,hdfid,'Latitude',lat
	
	scale_factor = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','scale_factor')
	offset = hdf_sd_attinfo(hdfid,'Optical_Depth_Land_And_Ocean','add_offset')
	hdf_sd_end,hdfid
	
	aod = (aod + offset.data(0))*scale_factor.data(0)
	nan = where(aod le 0. or aod ge 5.,nanc)
	if nanc gt 0 then aod(nan) = !values.f_nan

;	set_plot,'x'
;	loadct,39
;	device,decomposed=0
;	locidx = where(lat gt 20 and lat le 50 and lon gt 100 and lon le 145, locnum)
;	imagemap, aod(locidx), lat(locidx), lon(locidx), range=[0,2]
;	map_continents,/countries,/continents,color=0
;	map_grid,/box,latdel=5,londel=5

; endelse 

END
'''