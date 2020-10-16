import pytest

from src.lib.serializers.base_serializer import BaseSerializerError
from src.lib.serializers.customer_record_serializer import CustomerRecordSerializer
from src.models.customer import Customer
from src.models.customer_record import CustomerRecord
from src.models.location import Location


class TestCustomerRecordSerializer:

    @pytest.fixture(scope='session')
    def get_customer_record_serializer_obj(self):
        return CustomerRecordSerializer()

    @staticmethod
    def test_customer_record_serializer_with_invalid_data(get_customer_record_serializer_obj):
        with pytest.raises(BaseSerializerError) as exception_info:
            get_customer_record_serializer_obj.serialize(None)
        assert exception_info.value.message == "Serializer expects objects in an array format"

    @staticmethod
    def test_customer_record_serializer_with_empty_data(get_customer_record_serializer_obj):
        result = get_customer_record_serializer_obj.serialize([])
        assert len(result) == 0

    @staticmethod
    def test_customer_record_serializer_happy_scenario(get_customer_record_serializer_obj):
        data = CustomerRecord(Customer(user_id=1, name="Alice Cahill"), Location(latitude=51.92893, longitude=-10.27699))
        result = get_customer_record_serializer_obj.serialize([data])
        assert len(result) == 1
        assert result[0] == '{"customer": {"user_id": 1, "name": "Alice Cahill"}, "location": {"latitude": 51.92893, "longitude": -10.27699}}'