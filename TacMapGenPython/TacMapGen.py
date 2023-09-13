import matplotlib.pyplot as plt
import osmnx as osm
import numpy as np
import geopandas
import pandas

#IMPORT BOUNDING BOX
north = 41.466901
south = 41.462273
east = -74.09598
west = -74.102378

#COLORS
    #set 0 for color and 1 for BW
colorindex = 0
backgroundcolor = ['#7AC676', '#EEEEEE']
roadcolor = ['#644117', '#B4B4B4']
grasscolor = ['#BBEAB8', '#EAEAEA']
buildingcolor = ['#696969', '#939393']
watercolor = ['#aad3df', '#F1F1F1']

#TAG LIST
buildingtags = {'building': True}
grasstags = {'landuse': ['grass','recreation_ground']}
roadtags = {'highway': ['track', 'footway', 'service'], 'amenity': 'parking'}
watertags = {'natural': 'water'}

#IMPORT GEODATA
grass = osm.features_from_bbox(north, south, east, west, grasstags)
water = osm.features_from_bbox(north, south, east, west, watertags)
roads = osm.features_from_bbox(north, south, east, west, roadtags)
buildings = osm.features_from_bbox(north, south, east, west, buildingtags)

#CREATE PLOTS IN LAYERS
grassplot = grass.plot(color=grasscolor[colorindex])
waterplot = water.plot(ax=grassplot, color=watercolor[colorindex])
roadsplot = roads.plot(ax=waterplot, color=roadcolor[colorindex])
buildings = buildings.plot(ax=roadsplot, marker='o', color=buildingcolor[colorindex], markersize=5)

finalplot = buildings

#CUSTOMIZATION
finalplot.set_facecolor((backgroundcolor[colorindex]))
plt.grid(which='both', linestyle='-', lw=0.5, color='gray')
plt.xlim(west, east)
plt.ylim(south, north)

#TICK CALCULATIONS
    #How many gridlines
gridlines = 20

#NUMBERED GRIDLINES
ytickdiv = (north-south)/gridlines
xtickdiv = (east-west)/gridlines

yticklist = []
xticklist = []

for number in list(range(gridlines)):
    yticklist.append(south+ytickdiv*number)
    xticklist.append(west+xtickdiv*number)

#LETTER GRIDLINES
lastletter = 97 + gridlines
xticklabels = list(map(chr, range(97, lastletter)))
xticklabels = list(map(str.upper, xticklabels))

#GENERATING THE GRIDLINES
yticklabels = list(range(gridlines))
plt.yticks(yticklist, yticklabels)
plt.xticks(xticklist, xticklabels)

plt.show()