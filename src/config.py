import os
from src.models.location import Location

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EARTH_RADIUS_IN_KILOMETERS = 6371
DUBLIN_OFFICE_LOCATION = Location(53.339428, -6.257664)
INVITATION_RANGE_THRESHOLD_IN_KILOMETERS = 100
FILE_OUTPUT_PATH = ROOT_DIR + "/output"
CUSTOMER_RECORDS_FILE_PATH = ROOT_DIR + "/resources/customers.txt"

