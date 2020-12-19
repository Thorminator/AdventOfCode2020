def parse_input(file_name):
    with open(file_name) as f:
        return f.read().splitlines()


expressions = parse_input("example1.txt")


def consume_expression(expression):
    pass


def transform_operator(operator):
    if operator == "+":
        return lambda a, b: a + b
    elif operator == "*":
        return lambda a, b: a * b
    raise ValueError(f"Unknown operator: {operator}")


def consume_operator(txt):
    stripped = txt.strip()
    operator, rest = stripped[0], stripped[1:].strip()
    return transform_operator(operator), rest


def split_expression(expression):
    left, rest = consume_expression(expression)
    operator, rest = consume_operator(rest)
    right, _ = consume_expression(rest)


def evaluate_expression(expression):
    #TODO: Check if expression does not need to be split and just 'evaluate'
    left, operator, right = split_expression(expression)
    return operator(evaluate_expression(left), evaluate_expression(right))


result = sum(evaluate_expression(expression) for expression in expressions)
