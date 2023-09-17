import PySimpleGUI as sg
import matplotlib.pyplot as plt
import osmnx as osm

# Solves Blurry Font Issue
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# DEFAULT VALUES TO APPEAR IN INPUT AREAS
north = 41.466901
south = 41.462273
east = -74.09598
west = -74.102378
colorindex = 'COLOR'
gridlines = 20
labeled = 'YES'
exportformat = 'png'
quality = 300

# Declaring a theme
sg.theme('DarkGrey13')

# Window Setup
coordinates_column = [

    [sg.Text('TacMapGen 0.9.1 Instructions\n'
             '1) Enter your coordinates below in decimal form (XX.XXXXX)\n'
             '2) Set the appearance settings on the right hand side as required\n'
             '3) Set where you want the map file to go by clicking "Map Destination"\n'
             '4) Generate the map and send it to the destination by clicking "Generate"')],

    [sg.Text('COORDINATES')],

    [sg.Text('Enter the LATITUDE of the northeast corner of the mapped area.'),
        sg.InputText(north, s=(15, 22), key='north')],

    [sg.Text('Enter the LONGITUDE of the northeast corner of the mapped area.'),
        sg.InputText(east, s=(15, 22), key='east')],

    [sg.Text('Enter the LATITUDE of the southwest corner of the mapped area.'),
        sg.InputText(south, s=(15, 22), key='south')],

    [sg.Text('Enter the LONGITUDE of the southwest corner of the mapped area.'),
        sg.InputText(west, s=(15, 22), key='west')],
             ]

appearance_column = [
    [sg.Text('APPEARANCE')],

    [sg.Text('Do you want a colored or printer-friendly black and white map?\n(0 for COLOR, 1 for BW)'),
     sg.Combo(['COLOR', 'BLACK/WHITE'], default_value=colorindex, s=(15, 22), readonly=True, key='colorindex')],

    [sg.Text('How many grids do you want to the map to be divided into?'),
     sg.InputText(gridlines, s=(15, 22), key='gridlines')],

    [sg.Text('Do you want labels on points of interest?'),
     sg.Combo(['YES', 'NO'], default_value=labeled, s=(15, 22), readonly=True, key='labeled')],

    [sg.Text('What quality, in DPI, do you want the exported image to have?\n'
             'Default quality of 300dpi results in a 1,200x1,200 Image.\n'),
     sg.InputText(quality, s=(15, 22), key='quality')],

    [sg.FileSaveAs("Map Destination", key='save', enable_events=True,
                      file_types=(('PNG', '.png'), ('JPG', '.jpg'), ('SVG', '.svg'))),
     sg.Button('Generate')]]

layout = [
    [
        sg.Column(coordinates_column),
        sg.VSeperator(),
        sg.Column(appearance_column),
    ]
]

# CREATES THE WINDOW
window = sg.Window('TacMapGen 0.9.1 © Andriy Yatsykiv', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    north = float(values['north'])
    south = float(values['south'])
    east = float(values['east'])
    west = float(values['west'])

    colorindex = str(values['colorindex'])
    if colorindex == 'COLOR':
        colorindex = 0
    if colorindex == 'BLACK/WHITE':
        colorindex = 1

    gridlines = int(values['gridlines'])
    labeled = values['labeled']
    exportformat = str(values['exportformat'])
    quality = int(values['quality'])

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

    # CLEANS GEODATA
    # Preparing annotation dataframe from names
    names = names.loc['node', ['name', 'geometry']]

    # CREATE PLOTS IN LAYERS
    forestplot = forest.plot(color=forestcolor[colorindex])
    grassplot = grass.plot(ax=forestplot, color=grasscolor[colorindex])
    waterplot = water.plot(ax=grassplot, color=watercolor[colorindex])
    roadsplot = roads.plot(ax=waterplot, color=roadcolor[colorindex])
    buildingplot = buildings.plot(ax=roadsplot, marker='o', color=buildingcolor[colorindex], markersize=5)

    finalplot = buildingplot

    # RENDER LABELS FOR POIS
    if labeled == 'YES':
        for x, y, label in zip(names.geometry.x, names.geometry.y, names.name):
            # finalplot.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
            # The above is less customizable so I chose to use the below instead.
            finalplot.text(x, y, label.upper(), fontsize='x-small')

    # TICK CALCULATIONS

    # Calculates the division between ticks
    ytickdiv = (north - south) / gridlines
    xtickdiv = (east - west) / gridlines

    # Calculates 0.5 tick measurement for the minor tick offset
    half_y_tickdiv = ytickdiv / 2
    half_x_tickdiv = xtickdiv / 2

    # Sets the MAJOR ticks (for grid)
    yticklist = []
    xticklist = []

    for number in list(range(gridlines)):
        yticklist.append(south + ytickdiv * number)
        xticklist.append(west + xtickdiv * number)

        # Sets the MINOR ticks (for labels)
    yticklist_minor = []
    xticklist_minor = []

    for number in list(range(gridlines)):
        yticklist_minor.append(south + half_y_tickdiv + ytickdiv * number)
        xticklist_minor.append(west + half_x_tickdiv + xtickdiv * number)

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

    # PLOT EXPORT/SAVE
    plt.savefig(values["save"], bbox_inches='tight', dpi=quality)
    plt.show()

    if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
        break
