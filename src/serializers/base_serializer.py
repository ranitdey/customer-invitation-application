from abc import ABC, abstractmethod
from typing import List


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, objects: List):
        pass
