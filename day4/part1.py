import re

line_re = re.compile(r"(.*?):(.*)")
mandatory_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def parse_passports(file_name):
    result = []
    with open(file_name) as passport_file:
        current_passport = {}
        for line in passport_file:
            stripped_line = line.rstrip()
            if len(stripped_line) == 0:
                result.append(current_passport)
                current_passport = {}
            else:
                key_value_pairs = stripped_line.split(" ")
                current_passport.update({m.group(1): m.group(2) for m in
                                         [line_re.match(key_value_pair) for key_value_pair in key_value_pairs]})
    result.append(current_passport)
    return result


passports = parse_passports("input.txt")


def is_valid_passport(passport):
    return all(field in passport for field in mandatory_fields)


print(sum([1 for passport in passports if is_valid_passport(passport)]))
