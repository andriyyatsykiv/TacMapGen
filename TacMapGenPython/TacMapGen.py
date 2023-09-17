import matplotlib.pyplot as plt
import osmnx as osm
import numpy as np
import geopandas
import pandas

# USER SETTINGS
    #Asks user for color or black and white
#colorindex = int(input("Color or Black and White? Input 0 (Zero) for color or 1 for black and white:\n"))

    #Asks user for number of grid marks
#gridlines = int(input("How many grids do you want to the map to be divided into?\n"))

    #Asks user for POI labels or not.
#labeled = str(input("Do you want to label points of interest? (y/n)\nNOTE: Points of interest must
# be "nodes" (aka points) in OpenStreetMaps with a name attached to them."))

    #Asks user for export file format
    #Do you want to set a custom format (Default is .png) y/n
#exportformat = str(input('What format do you want your map to export as?\n Input "png" for png, 'jpg', 'svg'/n))

#quality = int(input('What quality, in DPI, do you want the exported image to have?/nA quality of 300dpi results in a 1,200x1,200 Image./n'

colorindex=0
gridlines=20
labeled = 'y'
exportformat = 'png'
quality = 300

# IMPORT BOUNDING BOX
north = 41.466901
south = 41.462273
east = -74.09598
west = -74.102378

# COLOR LIBRARY
    # set 0 for color and 1 for BW
forestcolor = ['#7AC676', '#FFFFFF']
roadcolor = ['#644117', '#7f7f7f']
grasscolor = ['#BBEAB8', '#EAEAEA']
buildingcolor = ['#696969', '#939393']
watercolor = ['#aad3df', '#dddbdb']

# TAG LIST
buildingtags = {'building': True}
grasstags = {'landuse': ['grass', 'recreation_ground']}
roadtags = {'highway': ['track', 'footway', 'service'], 'amenity': 'parking'}
watertags = {'natural': 'water'}
foresttags = {'natural': 'wood'}
nametags = {'name': True}

# IMPORT GEODATA
forest = osm.features_from_bbox(north, south, east, west, foresttags)
grass = osm.features_from_bbox(north, south, east, west, grasstags)
water = osm.features_from_bbox(north, south, east, west, watertags)
roads = osm.features_from_bbox(north, south, east, west, roadtags)
buildings = osm.features_from_bbox(north, south, east, west, buildingtags)
names = osm.features_from_bbox(north, south, east, west, nametags)

#CLEANS GEODATA
    #Preparing annotation dataframe from names
names = names.loc['node', ['name','geometry']]

# CREATE PLOTS IN LAYERS
forestplot = forest.plot(color=forestcolor[colorindex])
grassplot = grass.plot(ax=forestplot, color=grasscolor[colorindex])
waterplot = water.plot(ax=grassplot, color=watercolor[colorindex])
roadsplot = roads.plot(ax=waterplot, color=roadcolor[colorindex])
buildingplot = buildings.plot(ax=roadsplot, marker='o', color=buildingcolor[colorindex], markersize=5)

finalplot = buildingplot

#RENDER LABELS FOR POIS
if labeled == 'y':
    for x, y, label in zip(names.geometry.x, names.geometry.y, names.name):
        #finalplot.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
        #The above is less customizable so I chose to use the below instead.
        finalplot.text(x, y, label.upper(), fontsize='x-small')



# TICK CALCULATIONS

    # Calculates the division between ticks
ytickdiv = (north-south)/gridlines
xtickdiv = (east-west)/gridlines

    # Calculates 0.5 tick measurement for the minor tick offset
half_y_tickdiv = ytickdiv/2
half_x_tickdiv = xtickdiv/2

    # Sets the MAJOR ticks (for grid)
yticklist = []
xticklist = []

for number in list(range(gridlines)):
    yticklist.append(south+ytickdiv*number)
    xticklist.append(west+xtickdiv*number)

    # Sets the MINOR ticks (for labels)
yticklist_minor = []
xticklist_minor = []

for number in list(range(gridlines)):
    yticklist_minor.append(south+half_y_tickdiv+ytickdiv*number)
    xticklist_minor.append(west+half_x_tickdiv+xtickdiv*number)

    # LETTER GRIDLINES - Generates list of capital letters to use for letter labeling
lastletter = 97 + gridlines
xticklabels = list(map(chr, range(97, lastletter)))
xticklabels = list(map(str.upper, xticklabels))

    # NUMBERED GRIDLINES - Generates list of numbers for use with number labels
yticklabels = list(range(gridlines))

    # Creates the MINOR ticks for labeling
plt.yticks(yticklist_minor, yticklabels, minor=True)
plt.xticks(xticklist_minor, xticklabels, minor=True)

    # Creates the MAJOR ticks for the grid
    # Sets a blank list because otherwise labels are auto-written, even if labels=None
blank = []
plt.yticks(yticklist, blank)
plt.xticks(xticklist, blank)


# PLOT INITIALIZATION
# finalplot.set_facecolor((backgroundcolor[colorindex]))
plt.grid(which='major', linestyle='-', lw=0.5, color='grey')
plt.xlim(west, east)
plt.ylim(south, north)

#PLOT EXPORT/SAVE
plt.savefig(f'TacMapGen Map.{exportformat}', bbox_inches='tight', dpi=quality)
plt.show()