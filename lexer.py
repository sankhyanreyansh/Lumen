import token_

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
                self.token = token_.Operator(self.char)
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
        
        return token_.Integer(num) if not is_float else token_.Float(num)

    def advance(self):
        self.indx += 1
        if self.indx < len(self.text):
            self.char = self.text[self.indx]

