from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

while True:
    text = input(">>> ")
    if text == "exit":
        break
    
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    tree = parser.parse()
    
    interpreter = Interpreter(tree)
    result = interpreter.interpret()
    print(result)
