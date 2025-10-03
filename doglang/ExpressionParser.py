"""
Expression Parser with Operator Precedence
Implements a Pratt parser (operator precedence parser) for Doglang expressions.
This replaces the use of Python's eval() for improved security and control.
"""

from doglang.Tokenizer import Tokens


class ExpressionParser:
    """
    Parses and evaluates expressions using operator precedence parsing.
    
    Operator Precedence (highest to lowest):
    1. Parentheses: ()
    2. Unary operators: !, - (unary minus)
    3. Multiplicative: *, /, %
    4. Additive: +, -
    5. Comparison: <, >, <=, >=
    6. Equality: ==, !=
    7. Logical AND: &&
    8. Logical OR: ||
    """
    
    # Define operator precedence levels
    PRECEDENCE = {
        '||': 1,
        '&&': 2,
        '==': 3,
        '!=': 3,
        '<': 4,
        '>': 4,
        '<=': 4,
        '>=': 4,
        '+': 5,
        '-': 5,
        '*': 6,
        '/': 6,
        '%': 6,
    }
    
    def __init__(self, tokens, symbol_table=None):
        """
        Initialize the expression parser.
        
        Args:
            tokens: List of AST nodes representing the expression
            symbol_table: Symbol table for variable lookup (optional)
        """
        self.tokens = tokens
        self.symbol_table = symbol_table
        self.position = 0
    
    def current_token(self):
        """Get the current token without advancing."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None
    
    def advance(self):
        """Move to the next token."""
        self.position += 1
    
    def peek_token(self):
        """Look at the next token without advancing."""
        if self.position + 1 < len(self.tokens):
            return self.tokens[self.position + 1]
        return None
    
    def parse(self):
        """Parse and evaluate the expression."""
        result = self.parse_expression(0)
        
        # Validate that all tokens were consumed
        if self.position < len(self.tokens):
            remaining_token = self.tokens[self.position]
            raise Exception(
                f"Unexpected token '{remaining_token.value}' after expression. "
                f"Missing operator between operands?"
            )
        
        return result
    
    def parse_expression(self, min_precedence):
        """
        Parse expression using precedence climbing algorithm.
        
        Args:
            min_precedence: Minimum precedence level to consider
            
        Returns:
            Evaluated result of the expression
        """
        left = self.parse_primary()
        
        while True:
            token = self.current_token()
            if token is None:
                break
            
            # Check if current token is an operator
            if token.type not in [Tokens.ARITHMETIC_OP, Tokens.COMPARISON_OP, Tokens.LOGICAL_OP]:
                break
            
            op = token.value
            if op not in self.PRECEDENCE:
                break
            
            precedence = self.PRECEDENCE[op]
            if precedence < min_precedence:
                break
            
            self.advance()  # Consume the operator
            
            # Right associativity for same precedence (not needed for most operators)
            # For left associativity, we use precedence + 1
            right = self.parse_expression(precedence + 1)
            
            # Evaluate the operation
            left = self.evaluate_binary_op(left, op, right)
        
        return left
    
    def parse_primary(self):
        """
        Parse primary expressions (literals, identifiers, parenthesized expressions, unary ops).
        
        Returns:
            Evaluated result of the primary expression
        """
        token = self.current_token()
        
        if token is None:
            raise Exception("Unexpected end of expression")
        
        # Handle parenthesized expressions
        if token.type == Tokens.PARENTHESIS and token.value == '(':
            self.advance()  # Consume '('
            result = self.parse_expression(0)
            
            # Expect closing parenthesis
            if self.current_token() is None or self.current_token().value != ')':
                raise Exception("Missing closing parenthesis")
            self.advance()  # Consume ')'
            return result
        
        # Handle unary minus
        if token.type == Tokens.ARITHMETIC_OP and token.value == '-':
            self.advance()
            operand = self.parse_primary()
            return -operand
        
        # Handle logical NOT
        if token.type == Tokens.LOGICAL_OP and token.value == '!':
            self.advance()
            operand = self.parse_primary()
            return not operand
        
        # Handle integer literals
        if token.type == Tokens.INT_LITERAL:
            self.advance()
            return int(token.value)
        
        # Handle string literals
        if token.type == Tokens.STRING_LITERAL:
            self.advance()
            return token.value
        
        # Handle identifiers (variables)
        if token.type == Tokens.IDENTIFIER:
            self.advance()
            if self.symbol_table is None:
                raise Exception(f"Variable '{token.value}' used but symbol table not provided")
            
            symbol = self.symbol_table.lookup(token.value)
            if symbol is None:
                raise Exception(f"Variable '{token.value}' not declared")
            
            return symbol.value
        
        raise Exception(f"Unexpected token in expression: {token}")
    
    def evaluate_binary_op(self, left, op, right):
        """
        Evaluate a binary operation.
        
        Args:
            left: Left operand
            op: Operator string
            right: Right operand
            
        Returns:
            Result of the operation
        """
        # Arithmetic operators
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise Exception("Division by zero")
            # Integer division for int operands, float division otherwise
            if isinstance(left, int) and isinstance(right, int):
                return left // right
            return left / right
        elif op == '%':
            if right == 0:
                raise Exception("Modulo by zero")
            return left % right
        
        # Comparison operators
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        
        # Logical operators
        elif op == '&&':
            return left and right
        elif op == '||':
            return left or right
        
        else:
            raise Exception(f"Unknown operator: {op}")


def parse_and_evaluate(tokens, symbol_table=None):
    """
    Convenience function to parse and evaluate an expression.
    
    Args:
        tokens: List of AST nodes representing the expression
        symbol_table: Symbol table for variable lookup (optional)
        
    Returns:
        Evaluated result of the expression
    """
    parser = ExpressionParser(tokens, symbol_table)
    return parser.parse()
