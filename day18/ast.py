class AST:
    pass

class Operator(AST):
    def __init__(self, left, right, applier):
        self.left = left
        self.right = right
        self.applier = applier


class Number(AST):
    def __init__(self, val):
        self.val = val
