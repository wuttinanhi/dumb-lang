from typing import List
from node import Node, NumberNode, BinOpNode, ENodeType, EMathOperation, operation_coverter
from tokenizer import Tokenizer, Token, ETokenType


class Parser:
    def __init__(self, text: str) -> None:
        # text
        self.text = text

        # tokens
        self.tokenizer: Tokenizer = Tokenizer(self.text)
        self.tokens: List[Token] = self.tokenizer.tokenize()
        self.token_index: int = 0

        # nodes
        self.data_nodes: List[Node] = []
        self.operation_nodes: List[Node] = []

    def current_token(self):
        if self.token_index >= len(self.tokens):
            return None
        return self.tokens[self.token_index]

    def advance_token(self):
        if self.token_index + 1 >= len(self.tokens):
            self.token_index = self.token_index + 1
            return None

        self.token_index = self.token_index + 1
        next_token = self.tokens[self.token_index]
        return next_token

    def look_token(self, step=0):
        if self.token_index + step >= len(self.tokens):
            return None
        return self.tokens[self.token_index + step]

    def has_more_token(self):
        return self.token_index <= len(self.data_nodes)

    def parse_any(self, token: Token):
        if token.type == ETokenType.NUMBER:
            return self.parse_number(token)
        if token.type == ETokenType.OPERATOR:
            return self.parse_binop(token)

    def parse_number(self, token: Token):
        # number node
        if token.type == ETokenType.NUMBER:
            node = NumberNode(token.value)
            return node

    def parse_binop(self, token: Token):
        # binop node
        if token.type == ETokenType.OPERATOR:
            previous_node = self.data_nodes.pop()
            next_token = self.advance_token()
            right_node = self.parse_any(next_token)

            node = BinOpNode(
                operation=operation_coverter(token.value),
                left=previous_node,
                right=right_node,
            )

            return node

    def parse(self):
        while self.token_index <= len(self.tokens):
            current_token = self.current_token()

            if current_token is None:
                break

            node = self.parse_any(current_token)
            self.data_nodes.append(node)

            self.advance_token()

        return self.data_nodes


if __name__ == "__main__":
    parser = Parser("1+2+3 ")
    print(parser.parse()[0].exec())

    parser = Parser("5+5+10+10 ")
    print(parser.parse()[0].exec())

    parser = Parser("2*2-2 ")
    print(parser.parse()[0])
    print(parser.parse()[0].exec())
