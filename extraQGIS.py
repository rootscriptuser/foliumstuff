import folium
from folium.plugins import Geocoder, MousePosition
import json


map= folium.Map(tiles=None)

#folium.raster_layers.TileLayer(tiles='openstreetmap', name='my name').add_to(m)
'''
map=folium.Map(
    location=[45.92736, 14.972],
    zoom_start=8
    )
'''
#get name/(map id for use in scripts
map_id = map.get_name()
print("given map id: ",map_id)
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
        #popup='halo',
        #tooltip='<p id="samba">Url: {}</br>CallSign: {}</br>Type: {}'.format(url,callsing,type_),
        icon=folium.DivIcon(
        html='''
            <div>
                   <svg class="pin" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-broadcast" viewBox="0 0 16 16">
                    <path d="M3.05 3.05a7 7 0 0 0 0 9.9.5.5 0 0 1-.707.707 8 8 0 0 1 0-11.314.5.5 0 0 1 .707.707zm2.122 2.122a4 4 0 0 0 0 5.656.5.5 0 1 1-.708.708 5 5 0 0 1 0-7.072.5.5 0 0 1 .708.708zm5.656-.708a.5.5 0 0 1 .708 0 5 5 0 0 1 0 7.072.5.5 0 1 1-.708-.708 4 4 0 0 0 0-5.656.5.5 0 0 1 0-.708zm2.122-2.12a.5.5 0 0 1 .707 0 8 8 0 0 1 0 11.313.5.5 0 0 1-.707-.707 7 7 0 0 0 0-9.9.5.5 0 0 1 0-.707zM10 8a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"/>
                    </svg>     
            </div>
        '''.format(url,callsing,type_),
        icon_size=(100, 100),
        icon_anchor=(0, 0),  )
        ).add_to(map)



# Plugins for coordinates on mouse position
MousePosition(position='topright').add_to(map)

Geocoder().add_to(map)



folium.GeoJson('regions.json', name='regions', style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5",
    }).add_to(map)

#geo_map=map._repr_html_()
'''
            map_299002f1fee0aff0bd63360cbc7139a8.on('zoomend', function() {                        //triggers after zoom event
            let x = map_299002f1fee0aff0bd63360cbc7139a8.getZoom();     
                if (map_299002f1fee0aff0bd63360cbc7139a8.getZoom() >11){                        //where x is the zoom level where the change occurs
                console.log(x); //map.removeLayer(yourPolygon);
        }
        else {
                console.log(x); //map.addLayer(yourMarker);
        }
    }
'''
#map.get_root().html.add_child(folium.JavascriptLink('folium.js'))

map.save(outfile='fextraqgis.html')
print("map created and saved!")