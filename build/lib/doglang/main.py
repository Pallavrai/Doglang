from doglang.SymbolTable import SymbolTable
from doglang.SyntaxAnalyser import SyntaxAnalyser
from doglang.Tokenizer import Tokenizer
from doglang.SemanticAnalyser import SemanticAnalyser
from doglang.error import Error

class Interpreter:
    def __init__(self,code):
        self.symbol_table = SymbolTable()
        tokens=Tokenizer(code)
        parse=SyntaxAnalyser(tokens)
        ast=parse.parse()
        # SemanticAnalyser(ast)
        self.visit(ast)
    
    def visit(self,ast):
        if ast.type == "Program" or ast.type== "block":
            for child in ast.children:
                self.visit(child)

        elif ast.type == "assignment":
                self.assignment(ast.children)
        elif ast.type == "print":
                self.print_stmt(ast.children)
        elif ast.type == "loop":
                self.loop_stmt(ast.children)
        elif ast.type == "conditional":
                self.conditions(ast.children)

    def assignment(self,children):
         name = children[0].value
         if children[1].value == 'input':
              expression = children[1].children[0]
              prompt = self.expression_stmt(expression.children)
              val = input(prompt)
              self.symbol_table.insert(name=name,type=type(val),scope="local", value = val)
              return
         expression = self.expression_stmt(children[1].children)
         if self.symbol_table.lookup(name) is None:
              self.symbol_table.insert(name=name,type="int",scope="local", value = expression)
         else: #already exists variable just modify it
              self.symbol_table.modify(name=name,value = expression)
    
    def conditions(self,children):
         for child in children:
              if child.type == "expression":
                   check = self.expression_stmt(child.children)
                   if type(check) is bool:
                        if check:
                            self.visit(children[1].children[0])
                        else:
                             if len(children) > 2:
                                self.visit(children[2].children[0])
                   else:
                        Error("Type","Value inside sniff is not boolean.")
    
    def print_stmt(self,children):
            for child in children:
                if child.type == "expression":
                    result=self.expression_stmt(child.children)
                    print(result)
                    return result
            

    
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
          
            
    def expression_stmt(self,children):
        expression=""
        for child in children:
            if child.type == "STRING_LITERAL":
                 return child.value
            if child.type == "IDENTIFIER":
                if self.symbol_table.lookup(child.value) is None:
                    raise Exception("Variable not declared")
                else:
                    expression += str(self.symbol_table.lookup(child.value).value)
            else:
                expression += child.value
        return eval(expression)


