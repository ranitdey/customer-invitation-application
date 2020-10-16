from abc import ABC, abstractmethod
from typing import List


class BaseSerializerError(Exception):
    def __init__(self, message):
        self.message = message


class BaseSerializer(ABC):
    """
        Base serializer class for all serializer implementations.
    """
    @abstractmethod
    def serialize(self, objects: List):
        pass
