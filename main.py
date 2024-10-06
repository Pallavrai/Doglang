from SyntaxAnalyser import *

class Interpreter:
    def __init__(self,ast):
        self.ast=ast
    
    def visit(self):
         for child in self.ast.children: #visit program childs
             if child.type == "print":
                 print(child.children)


if __name__ == "__main__":
    code = "bark(x)"
    tokens=Tokenizer(code)
    print(tokens)
    parse=SyntaxAnalyser(tokens)
    ast=parse.parse()
    obj=Interpreter(ast)    
    obj.visit()