import json
from src.lib.deserializers.base_deserializer import BaseDeserializer, BaseDeserializerError
from src.models.customer import Customer, CustomerFields
from src.models.customer_record import CustomerRecord
from src.models.location import Location, LocationFields
from typing import List


class CustomerRecordDeserializer(BaseDeserializer):
    def deserialize(self, raw_data):
        if not isinstance(raw_data, List):
            raise BaseDeserializerError("Customer Record Deserializer expects raw input to be a list")
        deserialized_data = []
        for line in raw_data:
            data = json.loads(line)
            location = Location(float(data[LocationFields.latitude.name]), float(data[LocationFields.longitude.name]))
            customer = Customer(data[CustomerFields.user_id.name], data[CustomerFields.name.name])
            customer_record = CustomerRecord(customer, location)
            deserialized_data.append(customer_record)
        return deserialized_data
