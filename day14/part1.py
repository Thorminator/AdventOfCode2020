import re


def parse_input(file_name):
    with open(file_name) as f:
        return f.read().splitlines()


def to_binary(n):
    res = ""
    for i in reversed(range(0, 36)):
        bit = 2**i
        if n >= bit:
            res += "1"
            n -= bit
        else:
            res += "0"
    return res


class Program:
    mem_re = re.compile(r"mem\[(\d+)\]")

    def __init__(self, instructions):
        self.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.instructions = instructions
        self.memory = dict()

    def run(self):
        for instruction in self.instructions:
            self.__execute_instruction(instruction)
        return sum(self.memory.values())

    def __execute_instruction(self, instruction):
        name, value = (s.strip() for s in instruction.split("="))
        if name == "mask":
            self.__update_mask(value)
        else:
            self.__write_to_memory(name, value)

    def __update_mask(self, value):
        self.mask = value

    def __write_to_memory(self, name, value):
        m = Program.mem_re.match(name)
        if not m:
            raise ValueError(f"Unable to match {name} to memory expression")
        address = m.group(1)
        self.memory[address] = self.__apply_mask(value)

    def __apply_mask(self, value):
        bin_value = to_binary(int(value))
        masked_value = "".join(mask_char if mask_char != "X" else value_char for value_char, mask_char in zip(bin_value, self.mask))
        return int(masked_value, 2)


instructions = parse_input("input.txt")
program = Program(instructions)
print(program.run())
