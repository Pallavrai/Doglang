from doglang.SymbolTable import SymbolTable
from doglang.SyntaxAnalyser import SyntaxAnalyser
from doglang.Tokenizer import Tokenizer
from doglang.SemanticAnalyser import SemanticAnalyser
from doglang.error import SemanticError

class Interpreter:
    def __init__(self, code):
        # 1. Tokenize and Parse (Original Flow)
        tokens = Tokenizer(code)
        parser = SyntaxAnalyser(tokens)
        ast = parser.parse()

        # 2. Perform Semantic Analysis (New Step)
        analyser = SemanticAnalyser()
        analyser.check(ast)

        # 3. Interpret (Original Flow)
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
        result = self.expression_stmt(children[1].children)
        if self.symbol_table.lookup(name) is None:
            self.symbol_table.insert(name, "INT", result)
        else:
            self.symbol_table.modify(name, result)

    def conditions(self, children):
        check = self.expression_stmt(children[0].children)
        if check:
            self.visit(children[1])
        elif len(children) > 2:
            self.visit(children[2])
    
    def print_stmt(self, children):
        result = self.expression_stmt(children[0].children)
        print(result)

    def loop_stmt(self, children):
        condition_node = children[0]
        body_nodes = children[1:]
        while self.expression_stmt(condition_node.children):
            for node in body_nodes:
                self.visit(node)

    def expression_stmt(self, children):
        expression_str = ""
        for child in children:
            if child.type == "IDENTIFIER":
                symbol = self.symbol_table.lookup(child.value)
                expression_str += str(symbol.value)
            else:
                expression_str += str(child.value)
        return eval(expression_str)