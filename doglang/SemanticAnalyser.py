from doglang.SymbolTable import SymbolTable
from doglang.error import SemanticError

class SemanticAnalyser:
    """Walks the AST to check for logical errors."""
    def __init__(self):
        self.symbol_table = SymbolTable()

    def check(self, node):
        """Main entry point to start checking."""
        self.visit(node)

    def visit(self, node):
        """Calls the correct method for each node type."""
        method_name = f'visit_{node.type}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node.children:
            self.visit(child)
    
    def visit_Program(self, node):
        for child in node.children:
            self.visit(child)

    def visit_assignment(self, node):
        var_name = node.children[0].value
        expr_node = node.children[1]

        expression_type = self.visit(expr_node)
        self.symbol_table.insert(name=var_name, type=expression_type)

    def visit_expression(self, node):
        """Checks undeclared variables and determines expression type."""
        has_comparison = False
        if not node.children:
             raise SemanticError("Empty expression found.")

        for child in node.children:
            if child.type == 'IDENTIFIER':
                if not self.symbol_table.lookup(child.value):
                    raise SemanticError(f"Variable '{child.value}' is not defined.")
            if child.type == 'COMPARISON_OP':
                has_comparison = True
        return "BOOL" if has_comparison else "INT"

    def visit_print(self, node):
        if node.children:
            self.visit(node.children[0])

    def visit_loop(self, node):
        condition_node = node.children[0]
        if self.visit(condition_node) != "BOOL":
            raise SemanticError("Loop condition must be a boolean comparison.")
        for statement_node in node.children[1:]:
            self.visit(statement_node)

    def visit_conditional(self, node):
        condition_node = node.children[0]
        if self.visit(condition_node) != "BOOL":
            raise SemanticError("Sniff condition must be a boolean comparison.")
        
        self.visit(node.children[1]) 
        if len(node.children) > 2:
            self.visit(node.children[2]) 

    def visit_block(self, node):
        for statement in node.children:
            self.visit(statement)

    def visit_else(self, node):
        self.visit(node.children[0])