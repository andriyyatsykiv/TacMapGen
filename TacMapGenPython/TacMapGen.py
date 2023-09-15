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
colorindex = 1
backgroundcolor = ['#7AC676', '#b7b7b7']
roadcolor = ['#644117', '#7f7f7f']
grasscolor = ['#BBEAB8', '#EAEAEA']
buildingcolor = ['#696969', '#939393']
watercolor = ['#aad3df', '#dddbdb']

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

#TICK CALCULATIONS
    #How many gridlines
gridlines = 20

#NUMBERED GRIDLINES
ytickdiv = (north-south)/gridlines
xtickdiv = (east-west)/gridlines

half_y_tickdiv = ytickdiv/2
half_x_tickdiv = xtickdiv/2

#Sets the MAJOR ticks (for grid)
yticklist = []
xticklist = []

for number in list(range(gridlines)):
    yticklist.append(south+ytickdiv*number)
    xticklist.append(west+xtickdiv*number)

#Sets the MINOR ticks (for labels)
yticklist_minor = []
xticklist_minor = []

for number in list(range(gridlines)):
    yticklist_minor.append(south+half_y_tickdiv+ytickdiv*number)
    xticklist_minor.append(west+half_x_tickdiv+xtickdiv*number)

#LETTER GRIDLINES - Generates list of capital letters to use for letter labeling
lastletter = 97 + gridlines
xticklabels = list(map(chr, range(97, lastletter)))
xticklabels = list(map(str.upper, xticklabels))

#NUMBERED GRIDLINES - Generates list of numbers for use with number labels
yticklabels = list(range(gridlines))


#Creates the MINOR ticks for labeling
plt.yticks(yticklist_minor, yticklabels, minor=True)
plt.xticks(xticklist_minor, xticklabels, minor=True)

#Creates the MAJOR ticks for the grid
#Sets a blank list because otherwise labels are auto-written, even if labels=None
blank = []
plt.yticks(yticklist, blank)
plt.xticks(xticklist, blank)


#CUSTOMIZATION
finalplot.set_facecolor((backgroundcolor[colorindex]))
plt.grid(which='major', linestyle='-', lw=0.5, color='grey')
plt.xlim(west, east)
plt.ylim(south, north)

plt.show()