import ast


def parse_literal(value):
    return ast.literal_eval(value)
