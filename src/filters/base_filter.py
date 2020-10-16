from abc import ABC, abstractmethod
from src.models.customer_record import CustomerRecord


class BaseFilter(ABC):
    @abstractmethod
    def filter(self, customer_records: CustomerRecord, source, threshold):
        pass

