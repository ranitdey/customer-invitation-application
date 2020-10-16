from src.lib.utils.extractor import Extractor
from src.lib.utils.sorting import Sorting
from src.models.customer import Customer
from src.models.customer_record import CustomerRecord
from src.models.location import Location


class TestSorting:
    @staticmethod
    def test_reverse_ascending():
        customer_one = CustomerRecord(Customer(user_id=11, name="Alice Cahill"),
                                      Location(latitude=51.92893, longitude=-10.27699))
        customer_two = CustomerRecord(Customer(user_id=4, name="Ian Kehoe"),
                                      Location(latitude=53.2451022, longitude=-6.238335))
        customer_three = CustomerRecord(Customer(user_id=9, name="Alice Cahill"),
                                        Location(latitude=51.92893, longitude=-10.27699))
        data = [customer_one, customer_two, customer_three]
        extracted_data = Extractor.extract_customer(data)
        Sorting.sort_customers(extracted_data, True)
        assert len(extracted_data) == 3
        assert extracted_data[0].user_id <= extracted_data[1].user_id
        assert extracted_data[1].user_id <= extracted_data[2].user_id

