import folium
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode

# Example Romanian phone number
number = "X"

# Parse the number
parsed_number = phonenumbers.parse(number, "RO")

# Get country/region
location = geocoder.description_for_number(parsed_number, "en")

# Get carrier
service_provider = carrier.name_for_number(parsed_number, "en")

# Get timezone
time_zones = timezone.time_zones_for_number(parsed_number)

print(f"Location: {location}")
print(f"Carrier: {service_provider}")
print(f"Timezone: {time_zones}")

# OpenCage API key
key = 'X'

# Initialize OpenCage geocoder
geo_coder = OpenCageGeocode(key)

# Get the geographic coordinates and other information for the location
results = geo_coder.geocode(location)

# Print raw results for debugging
if results:
    print("Raw results from OpenCage:", results)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    # Extract city name if available
    components = results[0]['components']
    city = components.get('city') or components.get('town') or components.get('village')
    if not city:
        city = components.get('municipality') or components.get('locality')
    
    # Print latitude, longitude, and city name
    print(f"Latitude: {lat}, Longitude: {lng}, City: {city}")

    # Create a map centered at the extracted coordinates
    my_map = folium.Map(location=[lat, lng], zoom_start=9)

    # Add a marker to the map with city and location as popup
    folium.Marker([lat, lng], popup=f"{city if city else 'Unknown City'}, {location}").add_to(my_map)

    # Save the map to an HTML file
    my_map.save("mylocation.html")
else:
    print("Location could not be determined.")
