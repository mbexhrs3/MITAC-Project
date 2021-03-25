# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:56:12 2019

@author: mbexhrs3
"""

#!/usr/bin/env python
import numpy as np
from mpl_toolkits.basemap import Basemap, shiftgrid, addcyclic
import matplotlib
import matplotlib.pyplot as plt
import os
import matplotlib.colors as colors

from pyhdf.SD import SD, SDC


matplotlib.rcParams.update({'font.size': 15,'font.family':'Times New Roman'})


m_globe = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')



file_name = 'C:\Work\Aviation_Climate_Change\Data_Analysis\Data\MODIS\MOD06_L2.A2019233.0030.061.2019234225456.hdf'
geo_file_name = 'C:\Work\Aviation_Climate_Change\Data_Analysis\Data\MODIS\MOD03.A2019233.0030.061.2019233113716.hdf'

file = SD(file_name, SDC.READ)
geo_file = SD(geo_file_name,SDC.READ)

#print( file.info() )

#----------------------------------------------------------------------------------------#
# print SDS names

#datasets_dic = file.datasets()

#for idx,sds in enumerate(datasets_dic.keys()):
#    print( idx,sds )

#----------------------------------------------------------------------------------------#
# get data

sds_obj = file.select('Cirrus_Reflectance') # select sds

data = sds_obj.get() # get sds data

#print( data )

#----------------------------------------------------------------------------------------#
# get attributes

import pprint

pprint.pprint( sds_obj.attributes() )

for key, value in sds_obj.attributes().items():
    print( key, value )
    if key == 'add_offset':
        add_offset = value  
    if key == 'scale_factor':
        scale_factor = value

print( 'add_offset', add_offset, type(add_offset) )
print( 'scale_factor', scale_factor, type(scale_factor) )

data = (data - add_offset) * scale_factor

#print( data )


# get Lat data

sds_lat = geo_file.select('Latitude') # select sds

lat = sds_lat.get() # get sds data

print( lat )

# get Lon data

sds_lon = geo_file.select('Longitude') # select sds

lon = sds_lon.get() # get sds data

print( lon )






#from geotiepoints import modis5kmto1km

#lon1, lat1 = modis_5km_to_1km_geolocation data [1, 1]  







x, y = m_globe(lon, lat)
my_cmap = matplotlib.cm.get_cmap('rainbow')


cax = m_globe.pcolor(x,y,data,cmap=my_cmap,vmin=0.0,vmax=1.0)
plt.clim(vmin=0.0, vmax=1.0)
my_cmap.set_under('w')
#cax = m_globe.pcolor(x,y,T_DJF,shading='flat',cmap=my_cmap)
m_globe.drawcoastlines(linewidth=0.5)
#m_globe.drawcountries(linewidth=1.)
#m_globe.drawstates(linewidth=1., linestyle='solid', color='k')
m_globe.drawparallels(np.arange(-90.,91.,30.))
m_globe.drawmeridians(np.arange(-180.,180.,60.))
plt.title('a) Cirrus Reflectance')
cbar = m_globe.colorbar(cax, pad = 0.2, location='right',filled=True)
plt.savefig('Figure_1000.png',dpi=150)

















'''
#----------------------------------------------------------------------------------------#
# Exemple with Cloud_Mask_1km

sds_obj = file.select('Cloud_Mask_1km') # select sds

data = sds_obj.get()

pprint.pprint( sds_obj.attributes() )

print( data.shape )

#----------------------------------------------------------------------------------------#
# Extract info from a byte

import numpy as np

def bits_stripping(bit_start,bit_count,value):
    bitmask=pow(2,bit_start+bit_count)-1
    return np.right_shift(np.bitwise_and(value,bitmask),bit_start)

i = 576 # random pixel
j = 236

status_flag = bits_stripping(0,1,data[i,j,0]) 
day_flag = bits_stripping(3,1,data[i,j,0]) 
cloud_mask_flag = bits_stripping(1,2,data[i,j,0])

print( 'Cloud Mask determined: ',  status_flag )
print( 'Cloud Mask day or night: ',  day_flag )
print( 'Cloud Mask: ',  cloud_mask_flag )
'''

