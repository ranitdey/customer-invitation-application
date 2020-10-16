import pytest

from src.config import DUBLIN_OFFICE_LOCATION, INVITATION_RANGE_THRESHOLD_IN_KILOMETERS
from src.lib.filters.base_filter import BaseFilterError
from src.lib.filters.filter_by_distance import FilterByDistance
from src.models.customer import Customer
from src.models.customer_record import CustomerRecord
from src.models.location import Location


class TestFilterByDistance:

    @pytest.fixture(scope='session')
    def get_filter_by_distance_obj(self):
        return FilterByDistance()

    @staticmethod
    def test_filter_by_distance_with_wrong_customer_records(get_filter_by_distance_obj):
        with pytest.raises(BaseFilterError) as exception_info:
            get_filter_by_distance_obj.filter(None, DUBLIN_OFFICE_LOCATION, INVITATION_RANGE_THRESHOLD_IN_KILOMETERS)
        assert exception_info.value.message == "Filter expects customer records in for of an array"

    @staticmethod
    def test_filter_by_distance_with_none_source_location(get_filter_by_distance_obj):
        with pytest.raises(BaseFilterError) as exception_info:
            get_filter_by_distance_obj.filter([], None, INVITATION_RANGE_THRESHOLD_IN_KILOMETERS)
        assert exception_info.value.message == "Source location is not valid"

    @staticmethod
    def test_filter_by_distance_with_none_threshold(get_filter_by_distance_obj):
        with pytest.raises(BaseFilterError) as exception_info:
            get_filter_by_distance_obj.filter([], DUBLIN_OFFICE_LOCATION, None)
        assert exception_info.value.message == "Threshold is not valid"

    @staticmethod
    def test_filter_by_distance_happy_scenario(get_filter_by_distance_obj):
        customer_one = CustomerRecord(Customer(user_id=1, name="Alice Cahill"),
                                      Location(latitude=51.92893, longitude=-10.27699))
        customer_two = CustomerRecord(Customer(user_id=4, name="Ian Kehoe"),
                                      Location(latitude=53.2451022, longitude=-6.238335))

        result = get_filter_by_distance_obj.filter([customer_one, customer_two],
                                                   DUBLIN_OFFICE_LOCATION, INVITATION_RANGE_THRESHOLD_IN_KILOMETERS)

        assert len(result) == 1
        assert result[0].customer.user_id == 4
        assert result[0].customer.name == "Ian Kehoe"
        assert result[0].location.latitude == 53.2451022
        assert result[0].location.longitude == -6.238335
