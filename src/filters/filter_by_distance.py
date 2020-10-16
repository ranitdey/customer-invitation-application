from src.filters.base_filter import BaseFilter
from src.lib.computation import Computation
from src.models.customer_record import CustomerRecord


class FilterByDistance(BaseFilter):
    def filter(self, customer_records: CustomerRecord, source, threshold):
        filtered_data = []
        for record in customer_records:
            distance = Computation.compute_distance(source, record.location)
            if distance <= threshold:
                filtered_data.append(record)
        return filtered_data
