range_128 = [i for i in range(128)]
range_8 = [i for i in range(8)]

with open("input.txt") as in_file:
    seats = in_file.readlines()


def search(data, instructions, i):
    if len(data) == 1:
        return data[0]
    mid = int(len(data) / 2)
    if instructions[i] == "F" or instructions[i] == "L":
        return search(data[:mid], instructions, i + 1)
    else:
        return search(data[mid:], instructions, i + 1)


def calculate_seat_id(seat):
    row = search(range_128, seat[:7], 0)
    column = search(range_8, seat[7:], 0)
    return row * 8 + column


ids = [calculate_seat_id(seat) for seat in seats]
print(max(ids))
