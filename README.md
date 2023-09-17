# TacMapGen
OpenStreetMaps-driven Tactical Map Generation - ft. OSMnx and GeoPandas

Install
--------
Download the latest distribution, and run TacMapGen.exe from the main file.

![image](https://github.com/andriyyatsykiv/TacMapGen/assets/144859431/e757d939-94be-4094-b675-a50b16329c2c)


FAQ
---------
**"Nothing appears on my map, or some things are missing"**

TacMapGen processes the map data included in OpenStreetMaps (OSM) - which is like wikipedia, but for maps. If something doesn't appear, then it likely hasn't been mapped. I strongly encourage you to add the stuff you want mapped into OpenStreetMaps - It's incredibly easy (just dragging and dropping shapes onto sattelite imagery) and it helps the community tremendously. 

You can get started here - https://www.openstreetmap.org/

**"What things appear on the map?"**

TacMapGen parses the OpenStreetMaps (OSM) data for buildings, roads, grassy areas, forests, bodies of water, and points of interest that have a name associated with them (Called "nodes" in OSM with a "name" attribute). If it's not included in the above categories, it won't get mapped.
