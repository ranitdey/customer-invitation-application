import json
from typing import List
from src.models.customer_record import CustomerRecord
from src.serializers.base_serializer import BaseSerializer


class CustomerRecordSerializer(BaseSerializer):
    def serialize(self, objects: List[CustomerRecord]):
        serialized_data = []
        for customer_record in objects:
            serialized_data.append(json.dumps(customer_record, default=lambda o: o.__dict__))
        return serialized_data

