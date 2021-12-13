from typing import Dict, List

from src.line import Line
from src.token import ITokenType, Token
from src.modules.print import PrintModule
from src.modules.assign import AssignModule
from src.variable_storage import VariableStorage

class Context:
    def __init__(self, scripts: List[Token], variable_storage: VariableStorage, startAt: int = 0) -> None:
        self.__scripts = scripts
        self.__startAt = startAt
        self.__variable_storage = variable_storage
      

    def run(self):
        token = self.__scripts[self.__startAt]
        # print("=======================")
        # print(self.__startAt)
        # print(token.line.script)
        # print("=======================")

        if token.type == ITokenType.PRINT:
            PrintModule.execute(token, variable_storage=self.__variable_storage)
        if token.type == ITokenType.ASSIGN:
            AssignModule.execute(token, variable_storage=self.__variable_storage)

        # next context
        next_start = (self.__startAt + 1)

        if next_start == len(self.__scripts):
            # print("END")
            return

        next = Context(
            scripts=self.__scripts, 
            startAt=next_start, 
            variable_storage=self.__variable_storage
        )
        next.run()
