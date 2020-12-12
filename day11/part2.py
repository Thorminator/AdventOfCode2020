from copy import deepcopy


def parse_char(c):
    if c == ".":
        return None
    if c == "L":
        return 1


def parse_input(file_name):
    with open(file_name) as f:
        return [list(map(parse_char, line)) for line in f.readlines()]


def find_neighbour_in_direction(grid, i, j, row_diff, column_diff):
    distance = 1
    while 0 <= i + row_diff * distance < len(grid) and 0 <= j + column_diff * distance < len(grid[i + row_diff * distance]):
        row = i + row_diff * distance
        column = j + column_diff * distance
        if grid[row][column] is not None:
            return row, column
        else:
            distance += 1
    return None


def calculate_neighbours(grid, i, j):
    if grid[i][j] is None:
        return None

    result = []
    for row_diff in range(-1, 2):
        for column_diff in range(-1, 2):
            if row_diff == 0 and column_diff == 0:
                continue
            neighbour = find_neighbour_in_direction(grid, i, j, row_diff, column_diff)
            if neighbour is not None:
                result.append(neighbour)
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
    elif current == 1 and neighbour_sum >= 5:
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