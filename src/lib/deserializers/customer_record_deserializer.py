import json
from src.lib.deserializers.base_deserializer import BaseDeserializer, BaseDeserializerError
from src.models.customer import Customer, CustomerFields
from src.models.customer_record import CustomerRecord
from src.models.location import Location, LocationFields
from typing import List
import logging


class CustomerRecordDeserializer(BaseDeserializer):
    def deserialize(self, raw_data):
        """
        Deserializer method for Customer Records.This method deserializes json strings of customer records
        into objects of Customer Records.
        :param raw_data: List of json strings of customer records
        :return: List of Customer record objects
        """
        if not isinstance(raw_data, List):
            raise BaseDeserializerError("Customer Record Deserializer expects raw input to be a list")
        deserialized_data = []
        logging.info("Starting data deserialization")
        for line in raw_data:
            data = json.loads(line)
            location = Location(float(data[LocationFields.latitude.name]), float(data[LocationFields.longitude.name]))
            customer = Customer(data[CustomerFields.user_id.name], data[CustomerFields.name.name])
            customer_record = CustomerRecord(customer, location)
            deserialized_data.append(customer_record)
        logging.info("Deserialization completed")
        return deserialized_data
