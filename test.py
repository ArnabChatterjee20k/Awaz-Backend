# from api.utils.Notification import notify

# notify()

from api.Cache.Cache import Cache
from api.utils.generate_unique_id import generate_unique_id

from api.resources.Map.utils import distance_between_points

max_dist = 2000 #2km

long1=40.748817
lat1 = -73.985428

def with_max_dist():
    long2 = 40.74194307881312
    lat2 = -73.99423689009068
    return distance_between_points(lon1=long1,lon2=long2,lat1=lat1,lat2=lat2)


def outside_max_dist():
    long2 = 41.75792003351113
    lat2 = -74.02710601710008
    return distance_between_points(lon1=long1,lon2=long2,lat1=lat1,lat2=lat2)

print(round(with_max_dist()))
print(round(outside_max_dist()))

from api.utils.Token import create_access_token

print(create_access_token({"email":"arnabchatterjee.ac.2@gmail.com"}))
print(create_access_token({"email":"arnabchatterjee.ac.1@gmail.com"}))