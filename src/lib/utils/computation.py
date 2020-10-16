from math import acos, cos, sin, radians
from src.config import EARTH_RADIUS_IN_KILOMETERS
from src.models.location import Location
import logging


class ComputationError(Exception):
    def __init__(self, message):
        self.message = message


class Computation:
    @staticmethod
    def compute_distance(location_one: Location, location_two: Location):
        """
        Computes shortest distance between two points on a sphere.
        :param location_one: Location of the first point.
        :param location_two: Location of the second point.
        :return: Shortest distance between two points on a sphere
        """
        if not location_one or not location_two:
            raise ComputationError("Two locations are needed to calculate the distance")
        logging.info("Computing distance of point one (lat: {}, long: {}) and point two (lat: {}, long: {})".format(
            location_one.latitude, location_one.longitude, location_two.latitude, location_two.longitude))
        latitude_one = radians(location_one.latitude)
        longitude_one = radians(location_one.longitude)
        latitude_two = radians(location_two.latitude)
        longitude_two = radians(location_two.longitude)

        delta = abs(longitude_one - longitude_two)
        angle = acos((sin(latitude_one) * sin(latitude_two)) + (cos(latitude_one) * cos(latitude_two) * cos(delta)))
        logging.info("Distance computation completed")
        return angle * EARTH_RADIUS_IN_KILOMETERS
