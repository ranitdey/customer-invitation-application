from typing import List

from src.lib.filters.base_filter import BaseFilter, BaseFilterError
from src.lib.utils.computation import Computation
from src.models.customer_record import CustomerRecord
from src.models.location import Location


class FilterByDistance(BaseFilter):
    def filter(self, customer_records, source, threshold: float):
        filtered_data = []
        if not isinstance(customer_records, List):
            raise BaseFilterError("Filter expects customer records in for of an array")
        if not source or not isinstance(customer_records, List):
            raise BaseFilterError("Source location is not valid")
        if not threshold:
            raise BaseFilterError("Threshold is not valid")
        for record in customer_records:
            distance = Computation.compute_distance(source, record.location)
            if distance <= threshold:
                filtered_data.append(record)
        return filtered_data
