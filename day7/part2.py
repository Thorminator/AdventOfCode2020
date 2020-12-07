import re

line_re = re.compile(r"(.*) bags contain (.*)")
requirement_re = re.compile(r"\s*(\d+) (.+?) bag.*")


def parse_requirements_to_list(contains_string):
    requirements = contains_string.split(",")
    res = []
    for requirement in requirements:
        m = requirement_re.match(requirement)
        if m:
            res.append((int(m.group(1)), m.group(2)))
    return res


def add_requirement_to_dict(color, requirement_string, contains_dict):
    contains_dict[color] = parse_requirements_to_list(requirement_string)


def parse_rules(file_name):
    res = {}
    with open(file_name) as in_file:
        for line in in_file:
            m = line_re.match(line)
            add_requirement_to_dict(m.group(1), m.group(2), res)
    return res


def calculate_bags_in(bag):
    if len(rules[bag]) == 0:
        return 0

    new_bags = rules[bag]
    return sum(new_bag[0] + new_bag[0] * calculate_bags_in(new_bag[1]) for new_bag in new_bags)


rules = parse_rules("input.txt")
print(calculate_bags_in("shiny gold"))
