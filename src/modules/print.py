from typing import Dict
from src.token import Token
from src.modules.content import ContentParser
from src.variable_storage import VariableStorage

class PrintModule:
    @staticmethod
    def execute(token: Token, variable_storage: VariableStorage):
        # seperate text by space
        content = token.line.script.split(" ", 1)

        # parse content and print
        parsed = ContentParser.parse(content[1], variable_storage)

        # output to screen
        print(parsed)
