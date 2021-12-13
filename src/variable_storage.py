from typing import Dict


class VariableStorage:
    def __init__(self):
        self.__storage: Dict[str, any] = {}

    def get(self, key: str):
        return self.__storage[key]

    def set(self, key: str, value: any):
        self.__storage[key] = value

    def have_key(self, key: str):
        return key in self.__storage
