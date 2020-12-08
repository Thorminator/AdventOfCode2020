def to_instruction(line):
    split = line.split(" ")
    return split[0], int(split[1])


def parse_program(file_name):
    with open(file_name) as in_file:
        return tuple(to_instruction(line) for line in in_file.readlines())


def perform_instruction(instruction, index, memory, seen_indices):
    if index in seen_indices:
        return -1
    seen_indices.add(index)
    opcode, arg = instruction
    if opcode == "acc":
        memory["acc"] = memory["acc"] + arg
    elif opcode == "jmp":
        return index + arg
    return index + 1


def run_program(program, memory):
    index = 0
    seen_indices = set()
    while index != -1:
        index = perform_instruction(program[index], index, memory, seen_indices)
    return memory["acc"]


def start_program(program):
    return run_program(program, {"acc": 0})


print(start_program(parse_program("input.txt")))
