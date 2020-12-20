import unittest

example_files = (f"example{n}.txt" for n in range(1, 5))

class TestDay18(unittest.TestCase):
    def verify_examples(self):
        for example in example_files:
            with open(example) as f:
                split = f.read().split("\n")
