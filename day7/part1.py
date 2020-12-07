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


def add_or_create_entry(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]


def create_reverse_lookup(rule_dictionary):
    reverse_lookup_rules = {}
    for rule_bag, allowed_bags in rule_dictionary.items():
        for amount, bag in allowed_bags:
            add_or_create_entry(reverse_lookup_rules, bag, rule_bag)
    return reverse_lookup_rules


rules = parse_rules("input.txt")
reverse_lookup = create_reverse_lookup(rules)
result = set()
to_check = ["shiny gold"]
while not len(to_check) == 0:
    check_bag = to_check.pop()
    if check_bag in reverse_lookup:
        new_bags = reverse_lookup[check_bag]
        result = result.union(set(new_bags))
        to_check = to_check + new_bags
print(len(result))
