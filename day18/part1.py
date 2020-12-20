import re

number_re = re.compile(r"^\d+$")
operators = {"+", "*"}


def parse_input(file_name):
    with open(file_name) as f:
        return f.read().splitlines()


expressions = parse_input("example2.txt")


def consume_expression(txt):
    if is_number(txt):
        return txt, ""

    pars = 0
    for i, char in enumerate(txt):
        if char == "(":
            pars += 1
        elif char == ")":
            pars -= 1
            if pars == 0:
                return txt[:i+1], txt[i+1:]
        elif char in operators and pars == 0:
            return txt[:i], txt[i:]


def transform_operator(operator):
    if operator == "+":
        return lambda a, b: a + b
    elif operator == "*":
        return lambda a, b: a * b
    raise ValueError(f"Unknown operator: {operator}")


def consume_operator(txt):
    operator, rest = txt[0], txt[1:]
    return transform_operator(operator), rest


def is_number(txt):
    return number_re.match(txt) is not None


def split_expression(expression):
    left, rest = consume_expression(expression)
    operator, rest = consume_operator(rest)
    right, rest = consume_expression(rest)
    return left, right, operator, rest


def evaluate_expression(expression):
    expression = re.sub("\s", "", expression)
    if is_number(expression):
        return int(expression)

    left, right, operator, rest = split_expression(expression)
    return evaluate_expression(str(operator(evaluate_expression(left), evaluate_expression(right))) + rest)


print(sum(evaluate_expression(expression) for expression in expressions))
