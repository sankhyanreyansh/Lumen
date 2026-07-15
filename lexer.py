class Lexer:
    digits = "0123456789"
    operators = "+-*/"

    def __init__(self, text):
        self.text = text
        self.indx = 0
        self.char = self.text[self.indx]
        self.tokens = []
        self.token = None
    
    def tokenize(self):
        while self.indx < len(self.text):
            if self.char.isspace():
                self.advance()
                continue
            
            if self.char in Lexer.digits:
                self.token = self.extract_num()
            
            elif self.char in Lexer.operators:
                self.token = Operator(self.char)
                self.advance()

            self.tokens.append(self.token)

        return self.tokens

    def extract_num(self):
        num = ""
        is_float = False

        while (self.char in Lexer.digits or self.char == ".") and self.indx < len(self.text):
            if self.char == ".":
                is_float = True
            num += self.char
            self.advance()
        
        return Integer(int(num)) if not is_float else Float(float(num))

    def advance(self):
        self.indx += 1
        if self.indx < len(self.text):
            self.char = self.text[self.indx]


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"<{self.type_}> {self.value}"

class Operator(Token):
    def __init__(self, value):
        super().__init__("OP", value)

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLOAT", value)
