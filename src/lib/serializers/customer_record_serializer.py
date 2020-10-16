import json
from typing import List
from src.lib.serializers.base_serializer import BaseSerializer, BaseSerializerError
import logging


class CustomerRecordSerializer(BaseSerializer):
    def serialize(self, customer_record_objects):
        """
        This method serializes Customer Record objects to json formatted strings.
        :param customer_record_objects: List of Customer Record objects
        :return: List of json formatted strings of Customer Record objects
        """
        if not isinstance(customer_record_objects, List):
            raise BaseSerializerError("Serializer expects objects in an array format")
        serialized_data = []
        logging.info("Starting Serialization process")
        for customer_record in customer_record_objects:
            serialized_data.append(json.dumps(customer_record, default=lambda o: o.__dict__))
        logging.info("Serialization process completed")
        return serialized_data

