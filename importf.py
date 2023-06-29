import folium
from folium.plugins import Geocoder, MousePosition
from branca.element import Element

import json

# creating map object w/ degrees
map=folium.Map(
    location=[45.92736, 14.972],
    zoom_start=8
    )


#with open('nodes.json') as nodes:
#  nodes = nodes.read()
nodesfile = open('nodes.json', 'r')
nodes = json.load(nodesfile)
nodesfile.close()
#for x in nodes.keys('types'):
 # print(x)
#print(nodes)


for i in nodes:
    type_=(i['type'])
    callsing=(i['callsign'])
    name=(i['name'])
    url=(i['url'])
    coordinates=(i['coordinates'])
   
    folium.Marker(
        location=coordinates,
        #icon=folium.features.CustomIcon('router.png', icon_size=(50,50)),
        popup='halo',
        tooltip='<p>Url: {}</br>CallSign: {}</br>Type: {}'.format(url,callsing,type_),
        icon=folium.DivIcon(
        html='''
<span class="output">{}
</span>
        '''.format(name),
        icon_size=(100, 100),
        icon_anchor=(0, 0),  )
        ).add_to(map)



# Plugins for coordinates on mouse position
MousePosition(position='topright').add_to(map)

Geocoder().add_to(map)


'''
folium.GeoJson('regions.json', name='regions', style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5",
    }).add_to(map)
'''
#geo_map=map._repr_html_()

map.save(outfile='folium-map.html')
