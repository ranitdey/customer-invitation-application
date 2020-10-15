from src.models.customer import Customer
from src.models.location import Location


class CustomerRecord:
    def __init__(self, customer: Customer, location: Location):
        self.customer = customer
        self.location = location



