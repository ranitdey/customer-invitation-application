import pytest

from src.lib.deserializers.base_deserializer import BaseDeserializerError
from src.lib.deserializers.customer_record_deserializer import CustomerRecordDeserializer
from src.models.customer import Customer
from src.models.customer_record import CustomerRecord
from src.models.location import Location


class TestCustomerRecordDeserializer:

    @pytest.fixture(scope='session')
    def get_customer_record_deserializer_obj(self):
        return CustomerRecordDeserializer()

    @staticmethod
    def test_customer_record_deserializer_with_invalid_data(get_customer_record_deserializer_obj):
        with pytest.raises(BaseDeserializerError) as exception_info:
            get_customer_record_deserializer_obj.deserialize(None)
        assert exception_info.value.message == "Customer Record Deserializer expects raw input to be a list"

    @staticmethod
    def test_customer_record_deserializer_with_empty_data(get_customer_record_deserializer_obj):
        result = get_customer_record_deserializer_obj.deserialize([])
        assert len(result) == 0

    @staticmethod
    def test_customer_record_deserializer_happy_scenario(get_customer_record_deserializer_obj):
        raw_data = '{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}'
        result = get_customer_record_deserializer_obj.deserialize([raw_data])
        assert len(result) == 1
        assert isinstance(result[0], CustomerRecord)
        assert isinstance(result[0].customer, Customer)
        assert isinstance(result[0].location, Location)
        assert result[0].location.latitude == 51.92893
        assert result[0].location.longitude == -10.27699
        assert result[0].customer.user_id == 1
        assert result[0].customer.name == "Alice Cahill"


