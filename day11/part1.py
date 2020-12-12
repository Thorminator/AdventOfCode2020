from copy import deepcopy


def parse_char(c):
    if c == ".":
        return None
    if c == "L":
        return 1


def parse_input(file_name):
    with open(file_name) as f:
        return [list(map(parse_char, line)) for line in f.readlines()]


def calculate_neighbours(grid, i, j):
    if grid[i][j] is None:
        return None

    result = []
    for row in range(i-1, i+2):
        for column in range(j-1, j+2):
            if row == i and column == j:
                continue
            elif 0 <= row < len(grid) and 0 <= column < len(grid[row]):
                if grid[row][column] is not None:
                    result.append((row, column))
    return result


def calculate_neighbour_grid(grid):
    result = [[] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            result[i].append(calculate_neighbours(grid, i, j))
    return result


def calculate_grid_value(current, neighbours):
    if current is None:
        return None
    neighbour_sum = sum([grid[row][column] for row, column in neighbours]) if neighbours is not None else 0
    if current == 0 and neighbour_sum == 0:
        return 1
    elif current == 1 and neighbour_sum >= 4:
        return 0
    else:
        return current


def apply_rules(grid, neighbour_grid):
    new_grid = deepcopy(grid)
    changed = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current = grid[i][j]
            new_value = calculate_grid_value(current, neighbour_grid[i][j])
            new_grid[i][j] = new_value
            changed = changed or current != new_value
    return new_grid, changed


grid = parse_input("input.txt")


neighbour_grid = calculate_neighbour_grid(grid)
changed = True

while changed:
    grid, changed = apply_rules(grid, neighbour_grid)


def sum_ignoring_none(row):
    return sum(n for n in row if n is not None)


print(sum([sum_ignoring_none(row) for row in grid]))