# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from netCDF4 import*
import numpy as np
from mpl_toolkits.basemap import Basemap, shiftgrid, addcyclic
import matplotlib
import matplotlib.pyplot as plt
import os
import matplotlib.colors as colors

'''
from scipy.stats import t
import scipy.stats
from scipy import stats
import csv 
import seaborn as sns
sns.set(color_codes=True)
sns.set(font_scale=1.5)  # controls the font size in the plots

'''
'''
import cdo 
from cdo import *
cdo = Cdo()
cdo.debug = True
'''

matplotlib.rcParams.update({'font.size': 15,'font.family':'Times New Roman'})


m_globe = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')






filename ='C:\Work\Aviation Climate Change\Data_Analysis\Data\QUANTIFY\AircraftEmis_FL.nc'
#ncfile = Dataset(filename);
nc_file=Dataset(filename)
var_name = 'lat'
var_names = nc_file.variables.keys()
'''
Latitude = ncfile.variables['lat']
Longitude = ncfile.variables['lon']
FLevel = ncfile.variables['FL']
'''

lats=nc_file.variables['lat'][:]
lons=nc_file.variables['lon'][:]
lon, lat=np.meshgrid([lons],[lats])
alts = nc_file.variables['FL'][:]
nox = nc_file.variables['NOx'][:]
bc1 = nc_file.variables['BC'][:]
CO21 = nc_file.variables['CO2'][:]


N= np.sum(np.sum(nox,axis=0),axis=0)
bc= np.sum(np.sum(bc1,axis=0),axis=0)
CO2= (np.sum(np.sum(CO21,axis=0),axis=0))/1e6  #divided by 1e6 convert to Mkg/year

'''
#lons = nc_file.variables['lat'][:]
#lats = nc_file.variables['lon'][:]
Alt = nc_file.variables['FL'][:]
Lon, Lat=np.meshgrid([lons],[lats])
x, y = m_globe(Lon, Lat)
my_cmap = matplotlib.cm.get_cmap('rainbow')
cax = m_globe.pcolor(x,y,Alt[1],shading='flat',cmap=my_cmap)
m_globe.drawcoastlines(linewidth=0.5)


x, y = m_globe(Lon, Lat)
my_cmap = matplotlib.cm.get_cmap('rainbow')
cax = m_globe.pcolor(x,y,Alt,shading='flat',cmap=my_cmap,vmin=10,vmax=300)

'''


x, y = m_globe(lon, lat)
my_cmap = matplotlib.cm.get_cmap('rainbow')

#cax = m_globe.pcolor(lon,lat,N)
cax = m_globe.pcolor(x,y,N,cmap=my_cmap,vmin=5000,vmax=500000)
plt.clim(vmin=5000, vmax=500000)
my_cmap.set_under('w')
#cax = m_globe.pcolor(x,y,T_DJF,shading='flat',cmap=my_cmap)
m_globe.drawcoastlines(linewidth=0.5)
#m_globe.drawcountries(linewidth=1.)
#m_globe.drawstates(linewidth=1., linestyle='solid', color='k')
m_globe.drawparallels(np.arange(-90.,91.,30.))
m_globe.drawmeridians(np.arange(-180.,180.,60.))
plt.savefig('Figure_1.png',dpi=150)





fig=plt.figure(2001,figsize=(13,8))
fig.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.1,hspace=0.1)

ax = fig.add_subplot(221)
x, y = m_globe(lon, lat)
my_cmap = matplotlib.cm.get_cmap('rainbow')
cax = m_globe.pcolor(x,y,N,cmap=my_cmap,vmin=5000,vmax=500000)
plt.clim(vmin=5000, vmax=500000)
my_cmap.set_under('w')
#cax = m_globe.pcolor(x,y,T_DJF,shading='flat',cmap=my_cmap)
m_globe.drawcoastlines(linewidth=0.5)
#m_globe.drawcountries(linewidth=1.)
#m_globe.drawstates(linewidth=1., linestyle='solid', color='k')
m_globe.drawparallels(np.arange(-90.,91.,30.))
m_globe.drawmeridians(np.arange(-180.,180.,60.))
plt.gcf().subplots_adjust(wspace=0.1,hspace=0.19)
figure_title = ' '

ax2  = plt.subplot(2,2,1)       # this code increase gap between title and figure 
plt.text(0.5, 1.08, figure_title,
         horizontalalignment='center',
         fontsize=15,
         transform = ax2.transAxes)

cbar = m_globe.colorbar(cax, pad = 0.2, location='right',filled=True)

#plt.text(0.65, 1.3,'Surface temperature', horizontalalignment='left',verticalalignment='center', transform=ax2.transAxes,fontsize=25,color='k')
plt.text(0.0, 1.05,'a) NOx [kg(NO2)/year]', horizontalalignment='left',verticalalignment='center', transform=ax2.transAxes,fontsize=20,color='k')

ax = fig.add_subplot(222)
x, y = m_globe(lon, lat)
my_cmap = matplotlib.cm.get_cmap('rainbow')
cax = m_globe.pcolor(x,y,bc,cmap=my_cmap,vmin=100,vmax=6000)
plt.clim(vmin=100, vmax=6000)
my_cmap.set_under('w')
#cax = m_globe.pcolor(x,y,T_DJF,shading='flat',cmap=my_cmap)
m_globe.drawcoastlines(linewidth=0.5)
#m_globe.drawcountries(linewidth=1.)
#m_globe.drawstates(linewidth=1., linestyle='solid', color='k')
m_globe.drawparallels(np.arange(-90.,91.,30.))
m_globe.drawmeridians(np.arange(-180.,180.,60.))
plt.gcf().subplots_adjust(wspace=0.1,hspace=0.19)
figure_title = ' '

ax2  = plt.subplot(2,2,2)       # this code increase gap between title and figure 
plt.text(0.5, 1.08, figure_title,
         horizontalalignment='center',
         fontsize=15,
         transform = ax2.transAxes)

cbar = m_globe.colorbar(cax, pad = 0.2, location='right',filled=True)

#plt.text(0.65, 1.3,'Surface temperature', horizontalalignment='left',verticalalignment='center', transform=ax2.transAxes,fontsize=25,color='k')
plt.text(0.0, 1.05,'b) BC [kg/year]', horizontalalignment='left',verticalalignment='center', transform=ax2.transAxes,fontsize=20,color='k')


ax = fig.add_subplot(223)
x, y = m_globe(lon, lat)
my_cmap = matplotlib.cm.get_cmap('rainbow')
cax = m_globe.pcolor(x,y,CO2,cmap=my_cmap,vmin=10,vmax=900)
plt.clim(vmin=10, vmax=900)
my_cmap.set_under('w')
#cax = m_globe.pcolor(x,y,T_DJF,shading='flat',cmap=my_cmap)
m_globe.drawcoastlines(linewidth=0.5)
#m_globe.drawcountries(linewidth=1.)
#m_globe.drawstates(linewidth=1., linestyle='solid', color='k')
m_globe.drawparallels(np.arange(-90.,91.,30.))
m_globe.drawmeridians(np.arange(-180.,180.,60.))
plt.gcf().subplots_adjust(wspace=0.1,hspace=0.19)
figure_title = ' '

ax2  = plt.subplot(2,2,3)       # this code increase gap between title and figure 
plt.text(0.5, 1.08, figure_title,
         horizontalalignment='center',
         fontsize=15,
         transform = ax2.transAxes)

cbar = m_globe.colorbar(cax, pad = 0.2, location='right',filled=True)

#plt.text(0.65, 1.3,'Surface temperature', horizontalalignment='left',verticalalignment='center', transform=ax2.transAxes,fontsize=25,color='k')
plt.text(0.0, 1.05,'c) CO2 [Mkg/year]', horizontalalignment='left',verticalalignment='center', transform=ax2.transAxes,fontsize=20,color='k')
plt.text(0.90, 2.4,'Emissions (2000)', horizontalalignment='left',verticalalignment='center', transform=ax2.transAxes,fontsize=25,color='k')
plt.savefig('Figure_year_2000',dpi=150)
