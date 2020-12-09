import itertools


def parse_input(file_name):
    return [int(n) for n in open(file_name).readlines()]


def is_sum_of_two(number, candidates):
    for a, b in itertools.combinations(candidates, 2):
        if a + b == number:
            return True
    return False


def find_contiguous_set(numbers, target):
    added = []
    current = 0
    for n in numbers:
        added.append(n)
        current += n
        while current > target:
            removed = added.pop(0)
            current -= removed
        if current == target:
            return added
    return None


contiguous_set = find_contiguous_set(numbers=parse_input("input.txt"), target=133015568)
print(min(contiguous_set) + max(contiguous_set))
