from src.line import Line


class ITokenType:
    PRINT = "PRINT"
    ASSIGN = "ASSIGN"
    NONE = "NONE"
    COMMENT = "COMMENT"

class Token:
    def __init__(self, type: ITokenType, line: Line, value: any = None) -> None:
        self.type = type
        self.value = value
        self.line = line
