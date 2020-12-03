import itertools

numbers = []
with open("./input.txt") as in_file:
    for line in in_file:
        numbers.append(int(line))

for a, b, c in itertools.combinations(numbers, 3):
    if a + b + c == 2020:
        print(a * b * c)
