with open("input.txt") as in_file:
    grid = [line.rstrip() for line in in_file.readlines()]
max_x = len(grid[0])


def count_trees(step):
    x, y = 0, 0
    trees = 0
    while y + step[1] < len(grid):
        x, y = x + step[0], y + step[1]
        if grid[y][x % max_x] == "#":
            trees += 1
    return trees


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
for slope in slopes:
    product *= count_trees(slope)
print(product)
