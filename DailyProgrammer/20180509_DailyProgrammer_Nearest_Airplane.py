# https://www.reddit.com/r/dailyprogrammer/comments/8i5zc3/20180509_challenge_360_intermediate_find_the/
import urllib.request, json
from math import acos, sin, cos, radians, atan2
with urllib.request.urlopen("https://opensky-network.org/api/states/all") as url:
    data = json.loads(url.read().decode())['states']

EARTH_RAD = 6371

def geo_dist(x,y):
    xrad = [radians(d) for d in x]
    yrad = [radians(d) for d in y]
    return EARTH_RAD*acos(sin(xrad[0])*sin(yrad[0])+
                          cos(xrad[0])*cos(yrad[0])*
                          cos(abs(xrad[1]-yrad[1])))

def get_closest(longitude, lattitude):
    closest = data[0],10000000
    for plane in data:
        if None in plane[5:7]: continue
        dist = geo_dist(plane[5:7],[longitude,lattitude])
        if dist < closest[1]:
            closest = plane, dist
    
    print("closest plane to ",longitude,"E ",lattitude,"N")
    print("Geodesic distance:", closest[1])
    print("Callsign:", closest[0][1])
    print("Longitude and Lattitude:", closest[0][5],"E", closest[0][6],"N")
    print("Geometric Altitude:", closest[0][7])
    print("Country of origin:", closest[0][2])
    print("ICAO24 ID:", closest[0][0])

print("EIFEL TOWER\n------------")
get_closest(2.2945,48.8584)
print("\nJOHN F KENNEDY AIRPORT\n----------------------")
get_closest(-73.7781,40.6413)