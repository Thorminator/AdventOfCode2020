import re

line_re = re.compile(r"(.*?):(.*)")
height_re = re.compile(r"(\d+)(cm|in)$")
hcl_re = re.compile(r"#[0-9a-f]{6}$")
ecl_re = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)$")
pid_re = re.compile(r"[\d]{9}$")


def validate_height(height):
    m = height_re.match(height)
    if not m:
        return False
    unit = m.group(2)
    if unit == "cm":
        return 150 <= int(m.group(1)) <= 193
    elif unit == "in":
        return 59 <= int(m.group(1)) <= 76
    else:
        return False


def validate_hcl(hcl):
    return hcl_re.match(hcl)


def validate_ecl(ecl):
    return ecl_re.match(ecl)


def validate_pid(pid):
    return pid_re.match(pid)


field_validators = {"byr": lambda n: 1920 <= int(n) <= 2002, "iyr": lambda n: 2010 <= int(n) <= 2020,
                    "eyr": lambda n: 2020 <= int(n) <= 2030, "hgt": lambda h: validate_height(h),
                    "hcl": lambda hcl: validate_hcl(hcl), "ecl": lambda ecl: validate_ecl(ecl),
                    "pid": lambda pid: validate_pid(pid)}


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
    for field in field_validators:
        if field not in passport or not field_validators[field](passport[field]):
            return False
    return True


print(sum([1 for passport in passports if is_valid_passport(passport)]))
