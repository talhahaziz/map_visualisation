import folium
from folium.plugins import HeatMap

# Data for monitoring stations with average NO2 levels
station_data = [
    {'Station': 'Bootham', 'Latitude': 53.964784, 'Longitude': -1.088949, 'NO2': 15.03732667},
    {'Station': 'Fishergate', 'Latitude': 53.951928, 'Longitude': -1.074645, 'NO2': 26.87817378},
    {'Station': 'Fulford Road', 'Latitude': 53.943548, 'Longitude': -1.077012, 'NO2': 22.5693504},
    {'Station': 'Gillygate', 'Latitude': 53.964086, 'Longitude': -1.083812, 'NO2': 26.09809603},
    {'Station': 'Heworth Green', 'Latitude': 53.964536, 'Longitude': -1.070159, 'NO2': 26.34922746},
    {'Station': 'Holgate', 'Latitude': 53.955256, 'Longitude': -1.098494, 'NO2': 24.77962621},
    {'Station': 'Lawrence Street', 'Latitude': 53.955144, 'Longitude': -1.073315, 'NO2': 28.29719903},
    {'Station': 'Nunnery Lane', 'Latitude': 53.953991, 'Longitude': -1.089669, 'NO2': 24.60914678},
    {'Station': 'Plantation Drive', 'Latitude': 53.940318, 'Longitude': -1.095175, 'NO2': None},  # No data
]

# Create a map centered on York
york_map = folium.Map(location=[53.959, -1.081], zoom_start=13)

# Create a FeatureGroup for the pin-drops
pin_group = folium.FeatureGroup(name="Monitoring Stations")

# Add pin-drops for each station
for station in station_data:
    popup_text = f"<b>Station:</b> {station['Station']}<br><b>Avg NO2:</b> {station['NO2'] if station['NO2'] else 'No Data'}"
    folium.Marker(
        location=[station['Latitude'], station['Longitude']],
        popup=popup_text,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(york_map)

# Prepare data for HeatMap (excluding stations with no data)
heat_data = [
    [station['Latitude'], station['Longitude'], station['NO2']]
    for station in station_data if station['NO2'] is not None
]

# Create a FeatureGroup for the HeatMap
heat_group = folium.FeatureGroup(name="Pollution HeatMap")

# Adjust the HeatMap settings
HeatMap(heat_data, radius=50, blur=25, max_zoom=16).add_to(heat_group)

# Add groups to the map
heat_group.add_to(york_map)

# Add LayerControl to toggle between layers
folium.LayerControl().add_to(york_map)

# Save the map to an HTML file
york_map.save("york_air_quality_with_toggle_map.html")

# Display the map if running in a Jupyter Notebook
york_map