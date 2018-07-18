from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

#for install basemap
#conda install -c conda-forge basemap=1.0.8.dev0
#conda install -c conda-forge basemap-data-hires

# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
#axisbgc = ax.get_axis_bgcolor()
# setup mercator map projection.
m = Basemap(llcrnrlon=127.,llcrnrlat=34.,urcrnrlon=135.,urcrnrlat=44.01,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)
            
# nylat, nylon are lat/lon of New York
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon of London.
lonlat = 51.53; lonlon = 0.08
# draw great circle route between NY and London
#m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.drawcountries()
m.fillcontinents()
# draw parallels
m.drawparallels(np.arange(10,90,2),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,2),labels=[1,1,0,1])
#ax.set_title('Great Circle from New York to London')
plt.show()