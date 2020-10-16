from typing import List

from src.lib.filters.base_filter import BaseFilter, BaseFilterError
from src.lib.utils.computation import Computation
import logging


class FilterByDistance(BaseFilter):
    def filter(self, customer_records, source, threshold: float):
        """
        This method filters all locations which are within X kilometer away from the source location.Where X is defined
        as threshold.
        :param customer_records: List of Customer Record objects
        :param source: Source Location
        :param threshold: Threshold in kilometers for the filter
        :return: Filtered list of Customer Record objects
        """
        filtered_data = []
        if not isinstance(customer_records, List):
            raise BaseFilterError("Filter expects customer records in for of an array")
        if not source or not isinstance(customer_records, List):
            raise BaseFilterError("Source location is not valid")
        if not threshold:
            raise BaseFilterError("Threshold is not valid")
        logging.info("Filtering Customer Records started")
        for record in customer_records:
            distance = Computation.compute_distance(source, record.location)
            if distance <= threshold:
                filtered_data.append(record)
        logging.info("Filtering Customer Records completed")
        return filtered_data
