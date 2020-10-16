from abc import ABC, abstractmethod
from src.models.customer_record import CustomerRecord


class BaseFilterError(Exception):
    def __init__(self, message):
        self.message = message


class BaseFilter(ABC):
    @abstractmethod
    def filter(self, customer_records: CustomerRecord, source, threshold):
        pass
