import re

line_regex = re.compile(r"(\d+)-(\d+) (\w): (.*)")


def get_policy_and_password(line):
    match = line_regex.match(line)
    if not match:
        raise ValueError("Unmatched line: " + line)
    return int(match.group(1)) - 1, int(match.group(2)) - 1, match.group(3), match.group(4)


policies_and_passwords = []
with open("input.txt") as f:
    for input_line in f:
        policies_and_passwords.append(get_policy_and_password(input_line))


def is_valid_policy_and_password(policy_and_password):
    first_index, second_index, letter, password = policy_and_password
    if password[first_index:first_index + 1] == letter and password[second_index:second_index + 1] != letter:
        return True
    elif password[second_index:second_index + 1] == letter and password[first_index:first_index + 1] != letter:
        return True
    else:
        return False


valid_count = 0
for p in policies_and_passwords:
    if is_valid_policy_and_password(p):
        valid_count += 1
print(f"Valid passwords: {valid_count}")
