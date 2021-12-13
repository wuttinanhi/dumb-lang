from typing import Dict, List

from src.context import Context
from src.line import Line
from src.token import ITokenType, Token
from src.variable_storage import VariableStorage


class Interpreter:
    def __init__(self, scripts: List[str]):
        self.__scripts: List[Token] = self.__parse(scripts)
        self.__variable_storage: VariableStorage = VariableStorage()

    def execute(self):
        context = Context(self.__scripts, variable_storage=self.__variable_storage)
        context.run()

    def __parse(self, scripts: List[str]) -> List[Token]:
        tokens: List[Token] = []

        for index, code in enumerate(scripts):
            line = Line(index, code)
            token: Token = None
            
            if code.startswith("PRINT"):
                token = Token(type=ITokenType.PRINT, value=line, line=line)

            if code.startswith("SET"):
                token = Token(type=ITokenType.ASSIGN, value=line, line=line)

            if token == None:
                token = Token(type=ITokenType.NONE, line=line)
            
            tokens.append(token)

        return tokens
