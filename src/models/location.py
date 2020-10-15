from enum import Enum


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class LocationFields(Enum):
    latitude = "latitude"
    longitude = "longitude"
