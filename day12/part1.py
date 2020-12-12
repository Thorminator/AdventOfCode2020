class Ship:
    def __init__(self):
        self.degrees = 90
        self.x, self.y = 0, 0

    def forward(self, distance):
        self.move(self.get_direction(), distance)

    def move(self, direction, distance):
        self.x, self.y = self.x + direction[0] * distance, self.y + direction[1] * distance

    def get_direction(self):
        return 1 if self.degrees == 90 else -1 if self.degrees == 270 else 0, 1 if self.degrees == 0 else -1 if self.degrees == 180 else 0

    def rotate(self, action, amount):
        if action == "L":
            amount = -amount
        self.degrees = (self.degrees + amount) % 360


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

instructions = parse_input("input.txt")
ship = Ship()
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])
    if action in ("N", "S", "E", "W"):
        ship.move(direction_from_action(action), value)
    elif action in ("L", "R"):
        ship.rotate(action, value)
    elif action == "F":
        ship.forward(value)

print(abs(ship.x) + abs(ship.y))