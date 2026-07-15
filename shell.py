from lexer import Lexer

while True:
    text = input(">>> ")
    if text == "exit":
        break
    
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)
