from src.filters.base_filter import BaseFilter
from src.lib.computation import Computation
from src.models.customer_record import CustomerRecord
from src.models.location import Location


class FilterByDistance(BaseFilter):
    def filter(self, customer_records: CustomerRecord, criteria: dict):
        filtered_data = []
        for record in customer_records:
            distance = Computation.compute_distance(criteria["source"], record.location)
            if distance <= criteria["threshold"]:
                filtered_data.append(record)
        return filtered_data
