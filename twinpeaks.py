import folium

map = folium.Map(location=[	44.5124390, -103.8207070], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.CircleMarker(location=[44.5124390, -103.8207070], radius=6,fill_opacity=0.7, popup=("Hi, I am the coordinates"), fill_color='green', color="grey"))

map.add_child(fg)
map.save("tp.html") 
