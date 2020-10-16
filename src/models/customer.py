from enum import Enum


class Customer:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name


class CustomerFields(Enum):
    user_id = "user_id"
    name = "name"
