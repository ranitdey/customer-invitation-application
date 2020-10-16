from abc import ABC, abstractmethod
from typing import List


class BaseDeserializerError(Exception):
    def __init__(self, message):
        self.message = message


class BaseDeserializer(ABC):
    @abstractmethod
    def deserialize(self, raw_data):
        pass
