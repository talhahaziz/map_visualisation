import folium

# Data for monitoring stations
station_data = [
    {'Station': 'Bootham', 'Latitude': 53.964784, 'Longitude': -1.088949},
    {'Station': 'Fishergate', 'Latitude': 53.951928, 'Longitude': -1.074645},
    {'Station': 'Fulford Road', 'Latitude': 53.943548, 'Longitude': -1.077012},
    {'Station': 'Gillygate', 'Latitude': 53.964086, 'Longitude': -1.083812},
    {'Station': 'Heworth Green', 'Latitude': 53.964536, 'Longitude': -1.070159},
    {'Station': 'Holgate', 'Latitude': 53.955256, 'Longitude': -1.098494},
    {'Station': 'Lawrence Street', 'Latitude': 53.955144, 'Longitude': -1.073315},
    {'Station': 'Nunnery Lane', 'Latitude': 53.953991, 'Longitude': -1.089669},
    {'Station': 'Plantation Drive', 'Latitude': 53.940318, 'Longitude': -1.095175},
]

# Create a map centered on York
york_map = folium.Map(location=[53.959, -1.081], zoom_start=13)

# Add markers for each station
for station in station_data:
    popup_text = f"<b>Station:</b> {station['Station']}"
    folium.Marker(
        location=[station['Latitude'], station['Longitude']],
        popup=popup_text,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(york_map)

# Save the map to an HTML file
york_map.save("york_air_quality_map.html")

# Display the map if running in a Jupyter Notebook
york_map