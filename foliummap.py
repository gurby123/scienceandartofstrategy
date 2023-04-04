import folium
import json
import pandas as pd
import numpy as np
from folium.features import GeoJsonTooltip
from folium import plugins
import requests

# create a Folium map
m = folium.Map(location=[37.7749, -122.4194], zoom_start=4)

# create the base map layers
stamen_terrain = folium.TileLayer(tiles='http://tile.stamen.com/toner/{z}/{x}/{y}.png', name ='Stamen Toner', attr="toner-bcg").add_to(m)
osm = folium.TileLayer(tiles='http://tile.stamen.com/watercolor/{z}/{x}/{y}.jpg', name ='Watercolor', attr="toner-bcg").add_to(m)
sat = folium.TileLayer(tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', name = 'Satellite', attr="toner.bcg").add_to(m)
carto = folium.TileLayer(location=[-59.1759, -11.6016],tiles="cartodbpositron",zoom_start=2).add_to(m)
Stamen = folium.TileLayer(location=[-59.1759, -11.6016],tiles="Stamen Terrain",zoom_start=2).add_to(m)

#US Unemployment by States
url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
url1 = ( "https://raw.githubusercontent.com/gurby123/SEM/main" )
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url1}/US_Unemployment_Jan_2023.csv"state_data = pd.read_csv(state_unemployment)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", " "January 2023 unemployment rate""],
    key_on=" "feature.properties.name"",
    fill_color="YlGn",
    fill_opacity=0.4,
    line_opacity=.1,
    legend_name="Unemployment Rate (%)",
).add_to(m)

#African Continent Overlay created at geojson.io and stored online
overlay_url = 'https://raw.githubusercontent.com/gurby123/SEM/main/africaoverlay.json'
overlay = folium.GeoJson(overlay_url, name = 'Africa Overlay')


#HeatMap of Bike Station in Chicago
stations_url = 'https://gbfs.divvybikes.com/gbfs/en/station_information.json'

stations = json.loads(requests.get(stations_url).text)['data']['stations']
stations = pd.json_normalize(stations)
stations = stations[['lat', 'lon']]
stationArr = stations.values
bike_stations = folium.FeatureGroup(name='Bike Stations')
bike_stations.add_child(plugins.HeatMap(stationArr, radius=15))

# create a feature group for each layer
layer1 = folium.FeatureGroup(name='San Francisco')
circle = folium.CircleMarker(location=[17.5, 9.5], radius=35, color='blue', fill_color='yellow', name='Cicle').add_to(m)

# add markers to layer 1
layer1.add_child(folium.Marker(location=[37.7749, -122.4194], popup='San Francisco'))

# add each feature group to the map
m.add_child(layer1)
m.add_child(bike_stations)
m.add_child(overlay)

# add a layer control to the map
folium.LayerControl().add_to(m)

# display the map
m.save('map11.html') 
