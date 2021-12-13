from typing import Dict
from src.modules.content import ContentParser
from src.token import Token
from src.variable_storage import VariableStorage

class AssignModule:
    @staticmethod
    def execute(token: Token, variable_storage: VariableStorage):
        # split from equal
        ctx = token.line.script.split("=", 1)

        # left side is variable name
        variable_key = ctx[0]
        # remove "SET" word
        variable_key = variable_key.replace("SET", "")
        # strip space
        variable_key = variable_key.strip()

        # right side is variable content
        variable_content = ctx[1]
        # parse variable content
        variable_content = ContentParser.parse(raw=variable_content, variable_storage=variable_storage)

        # set to variable storage
        variable_storage.set(variable_key, variable_content)
