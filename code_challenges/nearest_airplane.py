from opensky_api import OpenSkyApi
from scipy.spatial import distance

api = OpenSkyApi()
states = api.get_states()

eiffel_tower = {'name' : 'Eiffel Tower', 'longitude' : 48.8584, 'latitude' : 2.2945, 'altitude' : 0}
jfk = {'name' : 'JFK', 'longitude' : 40.6413, 'latitude' : -73.7781, 'altitude' : 0}
destinations = [eiffel_tower, jfk]

# these not used yet
radius_of_earth_miles = 3959
radius_of_earth_kilometers = 6371

for s in states.states:
    for d in destinations:
        longitude = s.longitude
        latitude = s.latitude
        altitude = s.baro_altitude
        if None in (longitude, latitude, altitude):
            continue
        else:
            geodesic_distance = distance.euclidean([d['longitude'], d['latitude'], d['altitude']],[longitude, latitude, altitude])
            print("Flight {0} distance from {1} is {2}".format(s.callsign, d['name'], geodesic_distance))