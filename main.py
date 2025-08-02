import phonenumbers
from phonenumbers import geocoder, carrier
import opencage

number = "+201113866567"  # Replace with your real number
print("Phone Number:", number)
pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

service_provider = carrier.name_for_number(pepnumber, "en")
print("Service Provider:", service_provider)

from opencage.geocoder import OpenCageGeocode

key= "0ebdf19437ce4eaf8aba8abf6eee7745"

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
lat= result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print("Latitude:", lat)
print("Longitude:", lng)
import folium
map = folium.Map(location=[lat, lng], zoom_start=10)
folium.Marker([lat, lng], popup=location).add_to(map)
map.save("mymap.html")