import folium
import pandas
            #load data into variable
data = pandas.read_csv("Volcanoes.csv")
            #storing map in the variable
lat = list(data["LAT"])
lon = list(data["LON"])
vol_name = list(data["NAME"])
el = list(data["ELEV"])

def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'
            #storing map in the variable
map=folium.Map([48.777,-121], zoom_start=6,tiles="Stamen Terrain")
            #creating feature group
fgv=folium.FeatureGroup(name="Volcanoes")
            #adding child to fg with a marker
            #extracting both latutude and longitude simultaneously
for lt, ln, nm, el in zip(lat, lon, vol_name, el):
    #fg.add_child(folium.CircleMarker(location=[lt,ln], popup=nm +" "+ str(el) +"m" , icon=folium.Icon(color=color_producer(el),)))
    #use this for circle marker
    #color is grey that is ring color
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius =6, popup=nm +" "+ str(el) + "m", \
    fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7)) 
            #you may get a blank webpage if there are ' in the strings
            #for use popup=folium.Popup(str(el).parse_html=True)

fgp=folium.FeatureGroup(name="Population")

#for polygon layer create object using method
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))
#recent version of Folium needs a string instead of file as data input. Therefore you may need to add a read() method


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())    #layer control should be after feature group application
map.save("Map1.html")
