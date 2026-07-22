class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.indx = 0
        self.token = self.tokens[self.indx]

    def factor(self):
        if self.token.type_ == "INT" or self.token.type_ == "FLOAT":
            return self.token
        
    def term(self):
        left_node = self.factor()
        self.advance()

        while self.token.value in ("*", "/"):
            operator = self.token
            self.advance()
            right_node = self.factor()
            self.advance()
            left_node = [left_node, operator, right_node]

        return left_node

    def expression(self):
        left_node = self.term()

        while self.token.value in ("+", "-"):
            operator = self.token
            self.advance()
            right_node = self.term()
            left_node = [left_node, operator, right_node]

        return left_node

    def parse(self):
        return self.expression()

    def advance(self):
        self.indx += 1
        if self.indx < len(self.tokens):
            self.token = self.tokens[self.indx]