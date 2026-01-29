from astro_pi_orbit import ISS
import numpy as np
from time import sleep

iss = ISS()

def get_gps_coordinates(iss):
    """
    Returns a tuple of latitude and longitude coordinates expressed
    in signed degrees minutes seconds.
    """
    point = iss.coordinates()
    return (point.latitude.degrees, point.longitude.degrees)

coords1 = get_gps_coordinates(iss)
sleep(1)
coords2 = get_gps_coordinates(iss)
lat = np.radians(np.subtract(coords2[0], coords1[0]))
long = np.radians(np.subtract(coords2[1], coords1[1]))

a = np.sin(lat/2)+np.cos(coords2[0])*np.cos(coords1[0])*np.sin(long/2)
c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))
# dist = 6371*c

dist = np.sqrt((np.subtract(coords2[0], coords1[0])*111.3)**2+(np.subtract(coords2[1], coords1[1])*(111.3*(np.cos(np.subtract(coords2[1], coords1[1])))))**2)
print("speed: " + str(dist) + "km/s")
