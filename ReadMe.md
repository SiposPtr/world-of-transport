# Transport Hub Finder

This script finds transport hubs within a given distance from a specified location.

## Usage

1. Enter latitude, longitude, and search radius (km).
2. The script fetches transport hubs within the bounding box.
3. Results are sorted by distance.

## Functions

- **<a href="https://github.com/SiposPtr/world-of-transport/blame/main/main.py#L59-L70">calculate_distance(lat1, lon1, lat2, lon2)</a>**:<br>
Computes the great-circle distance using the Haversine formula.

- **<a href="https://github.com/SiposPtr/world-of-transport/blame/main/main.py#L73-L80">get_bounding_box(lat, lon, distance_km)</a>**:<br>
Determines min/max latitudes and longitudes for the search area.

- **<a href="https://github.com/SiposPtr/world-of-transport/blame/main/main.py#L83-L90">get_valid_float(prompt)</a>**:<br>
Ensures valid numeric input.

## Output
If transport hubs are found, they are displayed in ascending order of distance.

## Example input
```python
~/ ➤ python3.13 main.py
Enter your latitude: 21.50794    
Enter your longitude: 39.17006
Enter your distance (km): 25
```

## Expected output
```python
Transport Hubs Found:
- King Faisal Naval Base (21.3481, 39.173033), 17.78 km away
- King Abdulaziz Intl (21.679564, 39.156536), 19.13 km away
```