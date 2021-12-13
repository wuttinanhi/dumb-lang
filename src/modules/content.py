from typing import Dict

from src.variable_storage import VariableStorage


class ContentParser:
    @staticmethod
    def parse(raw: str, variable_storage: VariableStorage):
        # variable
        # string
        # math
        # boolean
        
        # variable section
        # check if variable
        # get key by trim raw
        key = raw.strip()
        # check is it variable
        if variable_storage.have_key(key) == True:
            return variable_storage.get(key)

        # string section
        # trim content
        content = raw.strip()

        # string remove quotes symbol
        return content[1:-1]
