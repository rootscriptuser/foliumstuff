import folium
import json
from geojson import Point, Feature, FeatureCollection, dump





nodesfile = open('nodes.json', 'r')
nodes = json.load(nodesfile)
nodesfile.close()

features = []

for i in nodes:
    type_=(i['type'])
    callsing=(i['callsign'])
    name=(i['name'])
    url=(i['url'])
    coordinates=(i['coordinates'])

    point = Point((coordinates))
    
    features.append(Feature(geometry=point))



# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as f:
   dump(feature_collection, f)
