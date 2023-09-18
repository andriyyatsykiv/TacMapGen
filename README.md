![GitHub License](https://img.shields.io/github/license/andriyyatsykiv/TacMapGen)
![GitHub top language](https://img.shields.io/github/languages/top/andriyyatsykiv/TacMapGen?style=plastic)
[![LoC](https://tokei.rs/b1/github/andriyyatsykiv/TacMapGen)](https://github.com/andriyyatsykiv/TacMapGen).
![GitHub last commit](https://img.shields.io/github/last-commit/andriyyatsykiv/TacMapGen?color=red&style=plastic)
[![Trello](https://img.shields.io/badge/Trello-TacMapGen-blue.svg)]([https://trello.com/b/KZuNuFjS/tacmapgen])

# TacMapGen
Easy Tactical Map Generation for outdoor competitive sports, with a specific focus on Airsoft and Paintball.

Install
--------
Download the latest distribution, and run TacMapGen.exe from the main file.

![Screenshot GUI](https://github.com/andriyyatsykiv/TacMapGen/assets/144859431/6cc8b3c2-a6d4-45f2-955f-38e5803046ba)

Examples
--------
![TMJT1](https://github.com/andriyyatsykiv/TacMapGen/assets/144859431/471c723b-12b5-4cac-a870-65770a4c4aad)
![BW](https://github.com/andriyyatsykiv/TacMapGen/assets/144859431/074324a2-d7aa-4c85-8674-d7ac2240276a)


FAQ
---------
**"Nothing appears on my map, or some things are missing"**

TacMapGen processes the map data included in OpenStreetMaps (OSM) - which is like wikipedia, but for maps. If something doesn't appear, then it likely hasn't been mapped. I strongly encourage you to add the stuff you want mapped into OpenStreetMaps - It's incredibly easy (just dragging and dropping shapes onto sattelite imagery) and it helps the community tremendously. 

You can get started here - https://www.openstreetmap.org/

**"What things appear on the map?"**

TacMapGen parses the OpenStreetMaps (OSM) data for buildings, roads, grassy areas, forests, bodies of water, and points of interest that have a name associated with them (Called "nodes" in OSM with a "name" attribute). If it's not included in the above categories, it won't get mapped.
