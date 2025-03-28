from SymbolTable import SymbolTable
from SyntaxAnalyser import SyntaxAnalyser
from Tokenizer import Tokenizer
from SemanticAnalyser import SemanticAnalyser

class Interpreter:
    def __init__(self):
        self.symbol_table = SymbolTable()
    
    def visit(self,ast):
        #  for child in ast.children: #visit program children
        #      if child.type == "print":
        #          return self.print_stmt(child.children)
        #      if child.type == "loop":
        #          return self.loop_stmt(child.children)
        if ast.type == "Program":
            for child in ast.children:
                self.visit(child)

        elif ast.type == "assignment":
                self.assignment(ast.children)
        elif ast.type == "print":
                self.print_stmt(ast.children)
        elif ast.type == "loop":
                self.loop_stmt(ast.children)

    def assignment(self,children):
         name = children[0].value
         expression = self.expression_stmt(children[1].children)
         if self.symbol_table.lookup(name) is None:
              self.symbol_table.insert(name=name,type="int",scope="local", value = expression)
         else: #already exists variable just modify it
              self.symbol_table.modify(name=name,value = expression)
    
    def print_stmt(self,children):
        for child in children:
            varName=child.value
            print(self.symbol_table.lookup(varName).value)

    
    def loop_stmt(self,children):
            # First, evaluate the condition
            condition_node = next((child for child in children if child.type == "expression"), None)
            body_nodes = [child for child in children if child.type != "expression"]
            
            if condition_node:
                condition = self.expression_stmt(condition_node.children)
                if condition:
                    # Execute the body of the loop
                    for node in body_nodes:
                        self.visit(node)
                    # Then check the condition again (recursively)
                    self.loop_stmt(children)
            else:
                 pass
                # If there's no condition, just
            
    def expression_stmt(self,children):
        expression=""
        for child in children:
            if child.type == "IDENTIFIER":
                if self.symbol_table.lookup(child.value) is None:
                    raise Exception("Variable not declared")
                else:
                    expression += str(self.symbol_table.lookup(child.value).value)
            else:
                expression += child.value
        return eval(expression)


if __name__ == "__main__":
    code = """  a=0
                wagtail(a<100){ 
                    bark(a)
                    a=a+10
                }
            """
    tokens=Tokenizer(code)
    parse=SyntaxAnalyser(tokens)
    ast=parse.parse()
    semantic = SemanticAnalyser(ast)
    obj=Interpreter()  
    obj.visit(ast)  
