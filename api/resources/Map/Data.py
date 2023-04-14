from os import environ
class MapEvent:
    danger = "DANGER"
    location = "LOCATION"
    max_dist = int(environ.get("DANGER_MAX_DISTANCE"))