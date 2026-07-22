class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return str(self.value)

class Operator(Token):
    def __init__(self, value):
        super().__init__("OP", value)

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", int(value))

class Float(Token):
    def __init__(self, value):
        super().__init__("FLOAT", float(value))