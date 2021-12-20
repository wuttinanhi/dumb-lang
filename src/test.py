from tokenizer import ETokenType, Tokenizer


def test():
    test1 = Tokenizer('PRINT "Hello, World!"')
    test1_tokens = test1.tokenize()
    assert test1_tokens[0].type == ETokenType.KEYWORDS
    assert test1_tokens[1].type == ETokenType.INDENT
    assert test1_tokens[2].type == ETokenType.STRING

    test2 = Tokenizer("123.45+123.456-.789")
    test2_tokens = test2.tokenize()
    # 123.45
    assert test2_tokens[0].type == ETokenType.NUMBER
    assert test2_tokens[0].value == 123.45

    # +
    assert test2_tokens[1].type == ETokenType.OPERATOR
    assert test2_tokens[1].value == "+"

    # 123.456
    assert test2_tokens[2].type == ETokenType.NUMBER
    assert test2_tokens[2].value == 123.456

    # -
    assert test2_tokens[3].type == ETokenType.OPERATOR
    assert test2_tokens[3].value == "-"

    # .789
    assert test2_tokens[4].type == ETokenType.NUMBER
    assert test2_tokens[4].value == 0.789

    print("ALL TEST PASSED!")


test()

# binop = BinOpNode(operation=EMathOperation.ADD, left=NumberNode(1), right=NumberNode(1))

# print(binop.exec())

# binop = BinOpNode(
#     operation=EMathOperation.MINUS, left=NumberNode(1), right=NumberNode(2)
# )

# print(binop.exec())

# binop = BinOpNode(
#     operation=EMathOperation.MULTIPLY,
#     left=BinOpNode(
#         operation=EMathOperation.ADD, left=NumberNode(1), right=NumberNode(2)
#     ),
#     right=NumberNode(3),
# )

# print(binop.exec())

# binop = BinOpNode(
#     operation=EMathOperation.ADD,
#     left=NumberNode(1),
#     right=BinOpNode(
#         operation=EMathOperation.MULTIPLY, left=NumberNode(2), right=NumberNode(3)
#     ),
# )

# print(binop.exec())
