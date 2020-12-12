class Ship:
    def __init__(self):
        self.x, self.y = 0, 0

    def forward(self, waypoint, amount):
        distance = waypoint[0] * amount, waypoint[1] * amount
        self.x, self.y = self.x + distance[0], self.y + distance[1]

def parse_input(file_name):
    with open(file_name) as f:
        return f.read().split("\n")

def direction_from_action(action):
    if action == "N":
        return 0, 1
    elif action == "S":
        return 0, -1
    elif action == "E":
        return 1, 0
    elif action == "W":
        return -1, 0
    else:
        print("Ups")

def move_waypoint(current, action, value):
    direction = direction_from_action(action)
    return current[0] + direction[0] * value, current[1] + direction[1] * value

def rotate_waypoint(current, action, rotation):
    if action == "L":
        rotation = 360 - rotation
    result = current
    while rotation > 0:
        rotation = rotation - 90
        result = (result[1], -result[0])
    return result


instructions = parse_input("input.txt")
ship = Ship()
waypoint = 10,1
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])
    if action in ("N", "S", "E", "W"):
        waypoint = move_waypoint(waypoint, action, value)
    elif action in ("L", "R"):
        waypoint = rotate_waypoint(waypoint, action, value)
    elif action == "F":
        ship.forward(waypoint, value)

print(abs(ship.x) + abs(ship.y))