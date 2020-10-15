from abc import ABC, abstractmethod


class BaseDeserializer(ABC):
    @abstractmethod
    def deserialize(self, raw_data):
        pass
