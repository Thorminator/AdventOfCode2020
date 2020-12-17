import functools
from copy import copy


class Rule:
    def __init__(self, name, matcher):
        self.name = name
        self.matcher = matcher

    def matches(self, value):
        return self.matcher(value)


def convert_to_matcher(validations):
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
        res.append(Rule(rule_name, convert_to_matcher(validations)))
    return res


def parse_tickets(ticket_lines):
    tickets = ticket_lines.splitlines()[1:]
    return [[int(n) for n in ticket.split(",")] for ticket in tickets]


def parse_input(file_name):
    with open(file_name) as f:
        inputs = f.read().split("\n\n")
        return parse_rules(inputs[0]), parse_tickets(inputs[1])[0], parse_tickets(inputs[2])


def is_valid_ticket(ticket, rules):
    for value in ticket:
        if all(not rule.matches(value) for rule in rules):
            return False
    return True


def get_matching_rules(field_index, tickets, rules):
    result = []
    for rule in rules:
        if all(rule.matches(ticket[field_index]) for ticket in tickets):
            result.append(rule)
    if len(result) == 0:
        raise ValueError("Unable to find matching rule")
    return result


available_rules, own_ticket, nearby_tickets = parse_input("input.txt")

valid_tickets = []
for nearby_ticket in nearby_tickets:
    if is_valid_ticket(nearby_ticket, available_rules):
        valid_tickets.append(nearby_ticket)

ticket_fields = dict()
undecided_rules = dict()
for i, field in enumerate(own_ticket):
    matching_rules = get_matching_rules(i, valid_tickets, available_rules)
    if len(matching_rules) == 1:
        matching_rule = matching_rules[0]
        available_rules.remove(matching_rule)
        ticket_fields[matching_rule.name] = field
    else:
        undecided_rules[i] = matching_rules

while len(undecided_rules) > 0:
    for field_index, potential_rules in copy(undecided_rules).items():
        for rule in copy(potential_rules):
            if rule not in available_rules:
                potential_rules.remove(rule)
        if len(potential_rules) == 1:
            rule = potential_rules[0]
            available_rules.remove(rule)
            ticket_fields[rule.name] = own_ticket[field_index]
            del undecided_rules[field_index]
print(functools.reduce(lambda a, b: a * b,
                       [ticket_fields[field] for field in ticket_fields.keys() if field.startswith("departure")]))
