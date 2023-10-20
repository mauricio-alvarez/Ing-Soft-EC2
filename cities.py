import pandas as pd
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


def getfromAPI(ciudad, pais):
    api = f'https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json'
    
    try:
        response = requests.get(api)
        response.raise_for_status()
        data = response.json()
        return data[0]
    except requests.exceptions.RequestException as e:
        print('Pais o ciudad no encontradas')
        print(e)

def getfromAPI(ciudad):
    api = f'https://nominatim.openstreetmap.org/search?q={ciudad}&format=json'
    
    try:
        response = requests.get(api)
        response.raise_for_status()
        data = response.json()
        return data[0]
    except requests.exceptions.RequestException as e:
        print('Pais o ciudad no encontradas')
        print(e)


data = pd.read_csv('worldcities.csv')
# Cities
to_city = "Lima"
from_city = "New York"
# find row of to_city and from_city
to_city_row = data[data['city'] == to_city]
from_city_row = data[data['city'] == from_city]
# find distance between to_city and from_city

lat1 = to_city_row["lat"].values[0]
lon1 = to_city_row["lng"].values[0]
lat2 = from_city_row["lat"].values[0]
lon2 = from_city_row["lng"].values[0]

# find haversine distance between to_city and from_city
print(haversine(lon1, lat1, lon2, lat2))