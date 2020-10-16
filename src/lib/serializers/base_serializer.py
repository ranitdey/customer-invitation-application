from abc import ABC, abstractmethod
from typing import List


class BaseSerializerError(Exception):
    def __init__(self, message):
        self.message = message


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, objects: List):
        pass
