import ast


def risky_eval(user_input):
    return ast.literal_eval(user_input)
