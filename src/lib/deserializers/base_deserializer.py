from abc import ABC, abstractmethod


class BaseDeserializerError(Exception):
    def __init__(self, message):
        self.message = message


class BaseDeserializer(ABC):
    """
    Base deserializer class for all deserializer implementations.
    """
    @abstractmethod
    def deserialize(self, raw_data):
        pass
