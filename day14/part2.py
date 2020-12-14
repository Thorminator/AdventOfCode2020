import itertools
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


def all_bit_combinations(combinations_so_far, bits_left):
    if bits_left <= 0:
        return combinations_so_far

    res = []
    for combination in combinations_so_far:
        res = res + all_bit_combinations([combination + "0", combination + "1"], bits_left - 1)
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
        write_addresses = self.__compute_write_addresses(int(m.group(1)))
        write_value = int(value)
        for write_address in write_addresses:
            self.memory[write_address] = write_value

    def __compute_write_addresses(self, address):
        masked_address = self.__apply_mask(address)
        num_of_floating_bits = masked_address.count("X")
        bit_combinations = self.__compute_bit_combinations_of_len(num_of_floating_bits)
        return [self.__apply_bit_combination(bit_combination, masked_address) for bit_combination in bit_combinations]

    def __apply_mask(self, value):
        bin_value = to_binary(value)
        return "".join(
            self.__get_char_after_mask(value_char, mask_char) for value_char, mask_char in zip(bin_value, self.mask))

    def __get_char_after_mask(self, value_char, mask_char):
        if mask_char == "0":
            return value_char
        elif mask_char == "1":
            return "1"
        else:
            return "X"

    def __compute_bit_combinations_of_len(self, num_of_floating_bits):
        return all_bit_combinations([""], num_of_floating_bits)

    def __apply_bit_combination(self, bit_combination, masked_address):
        next_bit_index = 0
        result = ""
        for char in masked_address:
            if char != "X":
                result += char
            else:
                result += bit_combination[next_bit_index]
                next_bit_index += 1
        return int(result, 2)


instructions = parse_input("input.txt")
program = Program(instructions)
print(program.run())
