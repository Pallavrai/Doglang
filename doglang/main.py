from doglang.SymbolTable import SymbolTable
from doglang.SyntaxAnalyser import SyntaxAnalyser
from doglang.Tokenizer import Tokenizer
from doglang.SemanticAnalyser import SemanticAnalyser
from doglang.error import DogLangError, SemanticError

class Interpreter:
    def __init__(self, code):
        # Your correct pipeline: Tokenize -> Parse -> Analyze
        tokens = Tokenizer(code)
        parser = SyntaxAnalyser(tokens)
        ast = parser.parse()

        analyser = SemanticAnalyser()
        analyser.check(ast)

        # Then, setup for interpretation
        self.symbol_table = SymbolTable()
        self.visit(ast)
    
    def visit(self, ast):
        if ast.type in ("Program", "block", "else"):
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

    def assignment(self, children):
        name = children[0].value
        # Keep the 'fetch' keyword (input) functionality from the main project
        if len(children) > 1 and hasattr(children[1], 'value') and children[1].value == 'input':
            expression = children[1].children[0]
            prompt = self.expression_stmt(expression.children)
            val = input(prompt)
            # Use your new SymbolTable's insert method
            self.symbol_table.insert(name=name, type=type(val), value=val)
            return
        
        expression = self.expression_stmt(children[1].children)
        if self.symbol_table.lookup(name) is None:
            # Use your new SymbolTable's insert method
            self.symbol_table.insert(name=name, type="int", value=expression)
        else:
            self.symbol_table.modify(name=name, value=expression)
    
    def conditions(self, children):
        # Keep the more robust conditions logic from the main project
        for child in children:
            if child.type == "expression":
                check = self.expression_stmt(child.children)
                if type(check) is bool:
                    if check:
                        self.visit(children[1].children[0])
                    elif len(children) > 2:
                        self.visit(children[2].children[0])
                else:
                    raise DogLangError("Type", "Value inside sniff is not boolean.")
    
    def print_stmt(self, children):
        for child in children:
            if child.type == "expression":
                result = self.expression_stmt(child.children)
                print(result)
                return result
            
    def loop_stmt(self, children):
        # Keep the improved iterative loop from the main project
        condition_node = next((child for child in children if child.type == "expression"), None)
        body_nodes = [child for child in children if child.type != "expression"]
        
        if condition_node:
            while self.expression_stmt(condition_node.children):
                for node in body_nodes:
                    self.visit(node)
            
    def expression_stmt(self, children):
        expression_str = ""
        for child in children:
            if child.type == "IDENTIFIER":
                # Adapt to use your object-based SymbolTable
                symbol = self.symbol_table.lookup(child.value)
                if symbol is None:
                    # This should not happen if the analyser works, but is a safeguard
                    raise Exception("Variable not declared")
                else:
                    expression_str += str(symbol.value)
            else:
                expression_str += str(child.value)
        return eval(expression_str)