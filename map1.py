import folium, pandas

data = pandas.read_csv("../app2-webmapping/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
lon = list(data["LON"])
names = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[36.022838,-115.080292], zoom_start=6)
#feature group
fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,name,el in zip(lat, lon, names,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6,fill_opacity=0.7, popup=("Hi, I am %s" %name), fill_color=color_producer(el), color = "grey"))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('../app2-webmapping/world.json', 'r', encoding='utf-8-sig'), style_function=lambda x: { 'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
