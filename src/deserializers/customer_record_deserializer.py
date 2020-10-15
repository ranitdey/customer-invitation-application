import json
from src.deserializers.base_deserializer import BaseDeserializer
from src.models.customer import Customer, CustomerFields
from src.models.customer_record import CustomerRecord
from src.models.location import Location, LocationFields


class CustomerRecordDeserializer(BaseDeserializer):
    def deserialize(self, raw_data):
        deserialized_data = []
        for line in raw_data:
            data = json.loads(line)
            location = Location(data[LocationFields.latitude.name], data[LocationFields.longitude.name])
            customer = Customer(data[CustomerFields.user_id.name], data[CustomerFields.name.name])
            customer_record = CustomerRecord(customer, location)
            deserialized_data.append(customer_record)
        return deserialized_data
