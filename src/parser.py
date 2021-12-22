from typing import List
from src.node import ModuleNode, Node, NumberNode, BinOpNode, ENodeType, EMathOperation, PrintNode, StringNode, operation_coverter
from src.tokenizer import Tokenizer, Token, ETokenType, OPERATOR


class Parser:
    def __init__(self, text: str) -> None:
        # text
        self.text = text

        # tokens
        self.tokenizer: Tokenizer = Tokenizer(self.text)
        self.tokens: List[Token] = self.tokenizer.tokenize()
        self.token_index: int = 0

        # nodes
        self.nodes: List[Node] = []

    def current_token(self):
        if self.token_index >= len(self.tokens):
            return None
        return self.tokens[self.token_index]

    def advance_token(self):
        self.token_index = self.token_index + 1

        if self.token_index >= len(self.tokens):
            return None

        next_token = self.tokens[self.token_index]
        return next_token

    def look_token(self, step=0):
        if self.token_index + step >= len(self.tokens):
            return None
        return self.tokens[self.token_index + step]

    def has_more_token(self):
        return self.token_index <= len(self.tokens)

    def parse(self):
        module = ModuleNode()

        while self.current_token() != None:
            # skip indent or newline
            if self.current_token().type in (ETokenType.INDENT, ETokenType.NEWLINE):
                self.advance_token()
                continue

            # parse print
            if self.current_token().type == ETokenType.KEYWORDS and self.current_token().value == ENodeType.PRINT:
                # skip space
                self.advance_token()
                self.advance_token()

                # parse print content
                print_value = self.parse_value()

                # create print node
                print_node = PrintNode(print_value)

                # add print node to module
                module.add_node(print_node)

                # go to next
                self.advance_token()
                continue

            # step to next token
            self.advance_token()

        return module
        # return self.parse_value()

    def parse_value(self):
        if self.current_token().type == ETokenType.STRING:
            string_node = StringNode(self.current_token().value)
            return string_node

        if self.current_token().type != ETokenType.NUMBER and self.current_token().value in OPERATOR == False:
            return None

        if self.current_token() == None:
            return None

        # START PARSING MATH EXPRESSION

        result = self.parse_expression()

        if self.current_token() != None:
            return result

        return result

    def parse_expression(self):
        result = self.parse_term()

        while self.current_token() != None and self.current_token().value in ("+", "-"):
            if self.current_token().value == "+":
                self.advance_token()

                result = BinOpNode(
                    operation=EMathOperation.ADD,
                    left=result,
                    right=self.parse_term(),
                )
            elif self.current_token().value == "-":
                self.advance_token()

                result = BinOpNode(
                    operation=EMathOperation.MINUS,
                    left=result,
                    right=self.parse_term(),
                )

        return result

    def parse_term(self):
        result = self.parse_factor()

        while self.current_token() != None and self.current_token().value in ("*", "/"):
            if self.current_token().value == "*":
                self.advance_token()

                result = BinOpNode(
                    operation=EMathOperation.MULTIPLY,
                    left=result,
                    right=self.parse_factor(),
                )
            elif self.current_token().value == "/":
                self.advance_token()

                result = BinOpNode(
                    operation=EMathOperation.DIVIDE,
                    left=result,
                    right=self.parse_factor(),
                )

        return result

    def parse_factor(self):
        token = self.current_token()

        if self.current_token().type == ETokenType.OPERATOR and self.current_token().value == "(":
            self.advance_token()
            result = self.parse_expression()

            if self.current_token().value != ")":
                raise SyntaxError("Invalid syntax!")

            self.advance_token()
            return result

        if self.current_token().type == ETokenType.NUMBER:
            self.advance_token()
            return NumberNode(token.value)

        if self.current_token().type == ETokenType.OPERATOR and self.current_token().value == "+":
            self.advance_token()
            return NumberNode(self.parse_factor())

        if self.current_token().type == ETokenType.OPERATOR and self.current_token().value == "-":
            self.advance_token()

            parse_factor: Node = self.parse_factor()
            parse_factor_value = parse_factor.exec()

            if str(parse_factor_value).startswith("-"):
                return NumberNode(abs(parse_factor_value))

            return NumberNode(-abs(parse_factor_value))

        raise SyntaxError("Invalid syntax!")


if __name__ == "__main__":
    parser = Parser("7-5+1")
    parsed_value = parser.parse_value().exec()
    assert parsed_value == 3

    parser = Parser("7-(5+1)")
    parsed_value = parser.parse_value().exec()
    assert parsed_value == 1

    parser = Parser("-(-5)")
    parsed_value = parser.parse_value().exec()
    assert parsed_value == 5
