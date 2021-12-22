from typing import List


class ENodeType:
    MODULE = "MODULE"
    NUMBER = "NUMBER"
    STRING = "STRING"
    BINOP = "BINOP"
    PRINT = "PRINT"
    ASSIGN = "ASSIGN"
    PARENTHESES = "PARENTHESES"
    IF = "IF"
    CONDITION = "CONDITION"
    BLOCK = "BLOCK"
    PRINT = "PRINT"


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


class ModuleNode(Node):
    def __init__(self, body: List[Node] = []) -> None:
        self.__type = ENodeType.MODULE
        self.__body = body

    def add_node(self, node: Node):
        self.__body.append(node)

    def exec(self):
        for node in self.__body:
            node.exec()
        return

    def __str__(self) -> str:
        return f"ModuleNode(body={len(self.__body)})"

    def __repr__(self) -> str:
        return self.__str__()


class NumberNode(Node):
    def __init__(self, value) -> None:
        self.__type = ENodeType.NUMBER

        if isinstance(value, Node):
            value = value.exec()

        if str(value).isdigit():
            self.__value = int(value)
        else:
            self.__value = float(value)

    def exec(self):
        return self.__value

    def __str__(self) -> str:
        return f"NumberNode(value={self.__value})"

    def __repr__(self) -> str:
        return self.__str__()


class StringNode(Node):
    def __init__(self, value) -> None:
        self.__type = ENodeType.STRING

        if isinstance(value, Node):
            value = value.exec()

        self.__value = value

    def exec(self):
        return self.__value

    def __str__(self) -> str:
        return f"StringNode(value={self.__value})"

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


class ParenthesesNode(Node):
    def __init__(self, content: Node) -> None:
        self.__type = ENodeType.PARENTHESES
        self.__content = content
        self.__value = None

    def exec(self):
        self.__value = self.__content.exec()
        return self.__value

    def __str__(self) -> str:
        return f"ParenthesesNode(content={self.__content})"

    def __repr__(self) -> str:
        return self.__str__()


class BlockStatementNode(Node):
    def __init__(self, body: List[Node]) -> None:
        self.__type = ENodeType.BLOCK
        self.__body = body

    def exec(self):
        for node in self.__body:
            node.exec()
        return

    def __str__(self) -> str:
        return f"BlockStatementNode(body={len(self.__body)})"

    def __repr__(self) -> str:
        return self.__str__()


class ConditionNode(Node):
    def __init__(self, compare: str, left: Node, right: Node) -> None:
        self.__type = ENodeType.CONDITION
        self.__left = left
        self.__right = right
        self.__compare = compare

    def exec(self) -> bool:
        # NEED IMPLEMENTATION
        pass

    def __str__(self) -> str:
        return f"ConditionNode(compare={self.__compare}, left={self.__left}, right={self.__right})"

    def __repr__(self) -> str:
        return self.__str__()


class IfNode(Node):
    def __init__(self, condition: ConditionNode, body: List[Node]) -> None:
        self.__type = ENodeType.IF
        self.__condition = condition
        self.__body = body

    def exec(self):
        if self.__condition == True:
            for node in self.__body:
                node.exec()
        return

    def __str__(self) -> str:
        return f"IfNode(condition={self.__condition},body={self.__body})"

    def __repr__(self) -> str:
        return self.__str__()


class PrintNode(Node):
    def __init__(self, value: Node) -> None:
        self.__type = ENodeType.PRINT
        self.__value = value

    def exec(self):
        return print(self.__value.exec())

    def __str__(self) -> str:
        return f"PrintNode(value={self.__value})"

    def __repr__(self) -> str:
        return self.__str__()


class AssignNode(Node):
    def __init__(self, key: str, value: Node) -> None:
        self.__type = ENodeType.ASSIGN
        self.__key = key
        self.__value = value

    def exec(self):
        # TO DO: assign variable to data store
        return

    def __str__(self) -> str:
        return f"AssignNode(key={self.__key},value={self.__value})"

    def __repr__(self) -> str:
        return self.__str__()
