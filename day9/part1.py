import itertools


def parse_input(file_name):
    return [int(n) for n in open(file_name).readlines()]


def is_sum_of_two(number, candidates):
    for a, b in itertools.combinations(candidates, 2):
        if a + b == number:
            return True
    return False


numbers = parse_input("input.txt")
preamble_length = 25
for i in range(preamble_length, len(numbers)):
    if not is_sum_of_two(numbers[i], numbers[i-preamble_length: i]):
        print(numbers[i])
        break
