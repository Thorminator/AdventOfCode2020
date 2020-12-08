from copy import copy


def to_instruction(line):
    split = line.split(" ")
    return split[0], int(split[1])


def parse_program(file_name):
    with open(file_name) as in_file:
        return list(to_instruction(line) for line in in_file.readlines())


def perform_instruction(program, index, memory, seen_indices):
    if index in seen_indices:
        return -2
    elif index == len(program):
        return -1

    instruction = program[index]
    seen_indices.add(index)
    name = instruction[0]
    if name == "acc":
        memory["acc"] = memory["acc"] + instruction[1]
    elif name == "jmp":
        return index + instruction[1]
    return index + 1


def run_program(program, memory):
    index = 0
    seen_indices = set()
    while index >= 0:
        index = perform_instruction(program, index, memory, seen_indices)
    return memory["acc"] if index == -1 else None


def start_program(program):
    return run_program(program, {"acc": 0})


def modify_instruction(initial_program, instruction_index, new_instruction):
    modified_program = copy(initial_program)
    modified_program[instruction_index] = (new_instruction, initial_program[instruction_index][1])
    return modified_program


def get_modified_instruction(program, instruction_index):
    instruction_name = program[instruction_index][0]
    if instruction_name == "nop":
        return "jmp"
    elif instruction_name == "jmp":
        return "nop"


def search_for_terminating_program(initial_program):
    found_value = None
    next_instruction_to_change = 0
    while found_value is None:
        new_instruction = get_modified_instruction(initial_program, next_instruction_to_change)
        if new_instruction:
            found_value = start_program(modify_instruction(initial_program, next_instruction_to_change, new_instruction))
        next_instruction_to_change += 1
    return found_value


print(search_for_terminating_program(parse_program("input.txt")))
