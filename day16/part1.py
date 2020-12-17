class Rule:
    def __init__(self, rule_name, validator):
        self.rule_name = rule_name
        self.validator = validator

    def validate(self, value):
        return self.validator(value)


def convert_to_validator(validations):
    min_max = [(int(validation[0]), int(validation[1])) for validation in map(lambda x: x.split("-"), validations)]
    return lambda n: any(low <= n <= high for low, high in min_max)


def parse_rules(rule_lines):
    rule_lines = rule_lines.splitlines()
    res = []
    for rule_line in rule_lines:
        split_rule = rule_line.split(":")
        rule_name = split_rule[0]
        validation_line = split_rule[1].strip()
        validations = validation_line.split(" or ")
        res.append(Rule(rule_name, convert_to_validator(validations)))
    return res


def parse_tickets(ticket_lines):
    tickets = ticket_lines.splitlines()[1:]
    return [[int(n) for n in ticket.split(",")] for ticket in tickets]


def parse_input(file_name):
    with open(file_name) as f:
        inputs = f.read().split("\n\n")
        return parse_rules(inputs[0]), parse_tickets(inputs[1])[0], parse_tickets(inputs[2])


rules, own_ticket, nearby_tickets = parse_input("input.txt")
error_rate = 0
for nearby_ticket in nearby_tickets:
    for field in nearby_ticket:
        if all(not rule.validate(field) for rule in rules):
            error_rate += field
print(error_rate)
