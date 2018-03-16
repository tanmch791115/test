__author__ = 'JSBZS-tanmch'
import time

start = time.clock()

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])

map = Basemap(llcrnrlon=80.33,
              llcrnrlat=3.01,
              urcrnrlon=138.16,
              urcrnrlat=56.123,
             resolution='h', projection='cass', lat_0 = 42.5,lon_0=120,ax=ax1)

shp_info = map.readshapefile("E:\\tools\\python\\basemap\\CHN_adm_shp\\CHN_adm1",'states',drawbounds=True)

for info, shp in zip(map.states_info, map.states):
    proid = info['NAME_1']
    if proid == 'Guangdong':
        poly = Polygon(shp,facecolor='g',edgecolor='c', lw=3)
        ax1.add_patch(poly)

map.shadedrelief()

map.drawcoastlines()
end=time.clock()
print(end-start)
plt.show()

