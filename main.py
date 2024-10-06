from SyntaxAnalyser import *

class Interpreter:
    def __init__(self,ast):
        self.ast=ast
    
    def visit(self):
         for child in self.ast.children: #visit program childs
             if child.type == "print":
                 return self.print_stmt(child.children)
    def print_stmt(self,children):
        for child in children:
            varName=child.value
            st=SymbolTable()
            print(st.lookup(varName).value)


if __name__ == "__main__":
    code = "x=34 bark(x)"
    tokens=Tokenizer(code)
    
    parse=SyntaxAnalyser(tokens)
    ast=parse.parse()
    obj=Interpreter(ast)    
    obj.visit()