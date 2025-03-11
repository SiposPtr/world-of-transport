import requests
import math
from math import radians, sin, cos, asin

def main():
    # getting input
    lat_input = get_valid_float("Enter your latitude: ")
    long_input = get_valid_float("Enter your longitude: ")
    dist_input = get_valid_float("Enter your distance (km): ")

    # calc bounding box
    min_lat, max_lat, min_lon, max_lon = get_bounding_box(lat_input, long_input, dist_input)

    # format the URL
    url = f"https://mikerhodes.cloudant.com/airportdb/_design/view1/_search/geo?query=lat:[{min_lat} TO {max_lat}] AND lon:[{min_lon} TO {max_lon}]"

    # make request
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return

    # check if request was successful
    if response.status_code == 200:
        data = response.json()
        # check if there are any transport hubs
        if not data.get("rows"):
            print("No transport hubs found in the given range.")
            return
        
        transport_hubs = []

        for row in data["rows"]:
            # get the name, lat, and lon of the transport hub
            name = row["fields"]["name"]
            lat = row["fields"]["lat"]
            lon = row["fields"]["lon"]

            # calc distance
            dist = calculate_distance(lat_input, long_input, lat, lon)
            # store the transport hub, latitute, longitude, and distance
            if dist <= dist_input:
                transport_hubs.append((name, lat, lon, dist))

        # sort transport hubs by ascending distance
        transport_hubs.sort(key=lambda x: x[3])
        
        # print the sorted transport hubs
        print("Transport Hubs Found:")
        for name, lat, lon, dist in transport_hubs:
            print(f"- {name} ({lat}, {lon}), {dist:.2f} km away")
    else:
        # handle errors
        print("Error:", response.status_code, response.text)

# function to calculate distance between two points
def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(math.sqrt(a))  # Corrected from acos
    radius_earth_km = 6371  # Earth's radius in km
    
    return radius_earth_km * c

# function to calculate bounding box
def get_bounding_box(lat, lon, distance_km):
    # calc the lat offset (1 degree of lat is 111 km)
    lat_offset = distance_km / 111.0
    # calc the long offset
    lon_offset = distance_km / (111.0 * cos(radians(lat)))
    # return the bounding box
    bounding_box = (lat - lat_offset, lat + lat_offset, lon - lon_offset, lon + lon_offset)
    return bounding_box

# function to get a valid float from the user
def get_valid_float(prompt):
    while True:
        try:
            # valid input, return the float
            return float(input(prompt))
        except ValueError:
            # invalid input, reprompt the user
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()