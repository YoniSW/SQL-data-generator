from math import sin, cos, sqrt, atan2, radians
import json

###########################################
''' CORDINATE SCRIPT'''
###########################################
'''
def cor_dist_calculator(lat1, lat2, lon1, lon2):
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance # Change to return result instead of printing

cities = {
  # city: N, E
  "Eilat":"29.5569348,34.9497949",
  "Beer-sheva":"31.2525238,34.7905787",
  "Holon":"32.0193121,34.7804076",
  "Tel-Aviv":"32.0804808,34.7805274",
  "Haifa":"32.8191218,34.9983856",
  "Jerusalem":"31.778345,35.2250786"
}

result = { } # result cache

for c1, o1 in cities.items():
  for c2, o2 in cities.items():
    if c1 == c2: # Skip distance to itself
      continue
    if c1 not in result:
      result[c1] = {}
    if c2 not in result:
      result[c2] = {}
    if c2 in result[c1]: # Skip calculation if result exists
      continue
    lat1, lon1 = o1.split(",")
    lat2, lon2 = o2.split(",")
    lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
    dist = cor_dist_calculator(radians(lat1), radians(lat2), radians(lon1), radians(lon2))
    result[c1][c2] = dist
    result[c2][c1] = dist

# Use JSON to pretty print
print(json.dumps(result, sort_keys=True, indent=4))

'''

city = {
    "Beer-sheva": {
        "Eilat": 189.21747275675654,
        "Haifa": 175.35050379031625,
        "Holon": 85.29517336117944,
        "Jerusalem": 71.5416191192519,
        "Tel-Aviv": 92.09843466978711
    },
    "Eilat": {
        "Beer-sheva": 189.21747275675654,
        "Haifa": 362.8819559061985,
        "Holon": 274.3674938933305,
        "Jerusalem": 248.48642279429794,
        "Tel-Aviv": 281.1587570076894
    },
    "Haifa": {
        "Beer-sheva": 175.35050379031625,
        "Eilat": 362.8819559061985,
        "Holon": 91.28659162472408,
        "Jerusalem": 117.7109871123201,
        "Tel-Aviv": 84.66537293562867
    },
    "Holon": {
        "Beer-sheva": 85.29517336117944,
        "Eilat": 274.3674938933305,
        "Haifa": 91.28659162472408,
        "Jerusalem": 49.81609716261069,
        "Tel-Aviv": 6.803793674263911
    },
    "Jerusalem": {
        "Beer-sheva": 71.5416191192519,
        "Eilat": 248.48642279429794,
        "Haifa": 117.7109871123201,
        "Holon": 49.81609716261069,
        "Tel-Aviv": 53.763653916915395
    },
    "Tel-Aviv": {
        "Beer-sheva": 92.09843466978711,
        "Eilat": 281.1587570076894,
        "Haifa": 84.66537293562867,
        "Holon": 6.803793674263911,
        "Jerusalem": 53.763653916915395
    }
}