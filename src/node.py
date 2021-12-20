class ENodeType:
    NUMBER = "NUMBER"
    STRING = "STRING"
    BINOP = "BINOP"
    PRINT = "PRINT"
    ASSIGN = "ASSIGN"


class EMathOperation:
    ADD = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


def operation_coverter(operation: str):
    if operation == "+":
        return EMathOperation.ADD
    if operation == "-":
        return EMathOperation.MINUS
    if operation == "*":
        return EMathOperation.MULTIPLY
    if operation == "/":
        return EMathOperation.DIVIDE


class Node:
    def exec(self):
        pass


class NumberNode(Node):
    def __init__(self, value) -> None:
        self.__type = ENodeType.NUMBER
        self.__value = value

    def exec(self):
        return self.__value

    def __str__(self) -> str:
        return f"NumberNode(value={self.__value})"

    def __repr__(self) -> str:
        return self.__str__()


class BinOpNode(Node):
    def __init__(self, operation: EMathOperation, left: Node, right: Node) -> None:
        self.__type = ENodeType.BINOP
        self.__operation = operation
        self.__left = left
        self.__right = right
        self.__value = None

    def exec(self):
        left_value = self.__left.exec()
        right_value = self.__right.exec()

        if self.__operation == EMathOperation.ADD:
            self.__value = left_value + right_value
        if self.__operation == EMathOperation.MINUS:
            self.__value = left_value - right_value
        if self.__operation == EMathOperation.MULTIPLY:
            self.__value = left_value * right_value
        if self.__operation == EMathOperation.DIVIDE:
            self.__value = left_value / right_value

        return self.__value

    def __str__(self) -> str:
        return f"BinOpNode(operation={self.__operation}, left={self.__left}, right={self.__right})"

    def __repr__(self) -> str:
        return self.__str__()
