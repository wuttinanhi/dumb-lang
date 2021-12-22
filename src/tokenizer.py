from typing import List
import re

KEYWORDS = ("SET", "IF", "THEN", "ELSE", "END", "PRINT")

OPERATOR = ("+", "-", "*", "/", "=", "(", ")")

NEWLINE = ("\r\n", "\n")

INDENT = ("\t", " ")


def is_newline(x: any):
    return x in NEWLINE


def is_indent(x: any):
    return x in INDENT


def is_keyword(x: str):
    return str(x) in KEYWORDS


def is_operator(x: str):
    return str(x) in OPERATOR


def is_valid_name(x: any):
    return re.search("^[A-Za-z0-9_-]*$", str(x)) != None


class ETokenType:
    OPERATOR = "OPERATOR"
    NEWLINE = "NEWLINE"
    INDENT = "INDENT"
    NUMBER = "NUMBER"
    STRING = "STRING"
    NAME = "NAME"
    KEYWORDS = "KEYWORDS"


class Token:
    def __init__(self):
        self.loc: int = None
        self.start: int = None
        self.end: int = None
        self.type: ETokenType = None
        self.value: str = None

    def __str__(self) -> str:
        if is_indent(self.value) == True:
            return f"Token(type={self.type}, value=<INDENT>, start={self.start}, end={self.end})"
        if is_newline(self.value) == True:
            return f"Token(type={self.type}, value=<NEWLINE>, start={self.start}, end={self.end})"
        return f'Token(type={self.type}, value="{self.value}", start={self.start}, end={self.end})'

    def __repr__(self) -> str:
        return self.__str__()


class Tokenizer:
    def __init__(self, raw: str) -> None:
        self.__text: str = raw
        self.__cursor: int = 0

    def current_position(self):
        return self.__cursor

    def set_position(self, position: int):
        self.__cursor = position

    def walk(self):
        self.__cursor = self.__cursor + 1
        if self.is_end() == True:
            return None
        next = self.__text[self.__cursor]
        return next

    def look(self, step=1):
        if self.__cursor + step >= len(self.__text):
            return None
        return self.__text[self.__cursor + step]

    def current_char(self):
        return self.look(0)

    def is_end(self):
        return self.__cursor >= len(self.__text)

    def tokenize(self):
        tokens: List[Token] = []

        while self.is_end() is False:
            # if nothing then exit loop
            if self.current_char() == None:
                break

            # type: NUMBER
            if str(self.current_char()).isnumeric() == True or str(self.current_char()) == ".":
                # number store
                number = ""

                # create token
                token = Token()
                token.type = ETokenType.NUMBER
                token.start = self.current_position()

                while str(self.current_char()).isnumeric() == True or str(self.current_char()) == ".":
                    number = number + self.current_char()
                    self.walk()

                token.end = self.current_position()

                # to int or float
                if number.isdigit() == True:
                    token.value = int(number)
                else:
                    if number.startswith(".") == True:
                        number = "0" + number
                    token.value = float(number)

                # add token to list
                tokens.append(token)

                # skip to next
                continue

            # type: OPERATOR
            if is_operator(self.current_char()) == True:
                # create token
                token = Token()
                token.type = ETokenType.OPERATOR
                token.start = self.current_position()
                token.value = str(self.current_char())
                token.end = self.current_position()

                # add token to list
                tokens.append(token)

                # walk to next
                self.walk()

                # skip to next
                continue

            # type: NEWLINE
            if is_newline(self.current_char()) == True:
                # create token
                token = Token()
                token.type = ETokenType.NEWLINE
                token.start = self.current_position()
                token.value = str(self.current_char())
                token.end = self.current_position()

                # add token to list
                tokens.append(token)

                # walk to next
                self.walk()

                # skip to next
                continue

            # type: INDENT
            if is_indent(self.current_char()) == True:
                # create token
                token = Token()
                token.type = ETokenType.INDENT
                token.start = self.current_position()
                token.value = str(self.current_char())
                token.end = self.current_position()

                # add token to list
                tokens.append(token)

                # walk to next
                self.walk()

                # skip to next
                continue

            # type: STRING
            if str(self.current_char()) == '"':
                # string store
                string = ""

                # create token
                token = Token()
                token.type = ETokenType.STRING
                token.start = self.current_position()

                while self.current_char() is not None:
                    string = string + str(self.current_char())
                    self.walk()

                    if str(self.current_char()) == '"':
                        string = string + str(self.current_char())
                        break

                token.value = str(string)
                token.end = self.current_position()

                # add token to list
                tokens.append(token)

                # walk to next
                self.walk()

                # skip to next
                continue

            # type: KEYWORD
            if type(self.current_char()) == str:
                # keyword store
                keyword = ""

                # create token
                token = Token()
                token.start = self.current_position()

                while (
                    type(self.current_char()) == str
                    and is_indent(self.current_char()) == False
                    and is_newline(self.current_char()) == False
                ):
                    keyword = keyword + self.current_char()
                    self.walk()

                    if is_keyword(keyword) == True:
                        break

                # skip if not KEYWORDS, maybe it is NAME
                if is_keyword(keyword) == True:
                    token.type = ETokenType.KEYWORDS
                    token.value = keyword
                    token.end = self.current_position()

                    # add token to list
                    tokens.append(token)

                    # skip to next
                    continue
                else:
                    # pass to type NAME
                    # also reset cursor
                    self.set_position(token.start)

            # type: NAME
            if type(self.current_char()) == str:
                # name store
                name = ""

                # create token
                token = Token()
                token.type = ETokenType.NAME
                token.start = self.current_position()

                while type(self.current_char()) == str:
                    if is_indent(self.current_char()) == True:
                        break

                    if is_newline(self.current_char()) == True:
                        break

                    if is_operator(self.current_char()) == True:
                        break

                    name = name + self.current_char()
                    self.walk()

                if is_valid_name(name) == True:
                    token.value = name
                    token.end = self.current_position()

                    # add token to list
                    tokens.append(token)

                    # skip to next
                    continue
                else:
                    # if not valid throws error
                    raise NameError(f'Invalid name: "{name}"')

            # if unknown throw error
            raise SyntaxError(f'Invalid syntax: "{self.current_char()}"')

        return tokens


if __name__ == "__main__":
    # tokenizer = Tokenizer("123.456+.456")

    # tokenizer = Tokenizer('"Hello, World!" + (123-456.789)')

    # tokenizer = Tokenizer('SET name = (("Hello, World!") + (123-456.789))')

    tokenizer = Tokenizer('PRINT "Hello, World!"')

    tokens = tokenizer.tokenize()

    for token in tokens:
        print(token)
