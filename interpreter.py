import token_

class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def compute_binary(self, left_node, operator, right_node):
        output = None
        if operator.value == "+":
            output = left_node.value + right_node.value
        elif operator.value == "-":
            output = left_node.value - right_node.value
        elif operator.value == "*":
            output = left_node.value * right_node.value
        elif operator.value == "/":
            return token_.Float(left_node.value / right_node.value)

        return token_.Float(output) if left_node.type_ == "FLOAT" or right_node.type_ == "FLOAT" else token_.Integer(output)

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1]

        return self.compute_binary(left_node, operator, right_node)