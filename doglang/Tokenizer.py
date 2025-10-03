import re
# Import your new custom exception
from .error import DogLangSyntaxError


class Token:
    def __init__(self, token_type, value, line): # Added line number
        self.token_type = token_type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"\nToken({self.token_type}, '{self.value}', line={self.line})"


class Tokens:
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    ASSIGNMENT_OP = 'ASSIGNMENT_OP'
    # ... (rest of your Tokens class is fine) ...
    INT_LITERAL= 'INT_LITERAL'
    STRING_LITERAL='STRING_LITERAL'
    ARITHMETIC_OP = 'ARITHMETIC_OP'
    COMPARISON_OP = 'COMPARISON_OP'
    LOGICAL_OP = 'LOGICAL_OP'
    SEPARATOR = 'SEPARATOR'
    PARENTHESIS = 'PARENTHESIS'
    CURLY_BRACE = 'CURLY_BRACE'
    SEMICOLON = 'SEMICOLON'
    COMMENT = 'COMMENT'

keywords = {'bark', 'wagtail', 'fetch', 'sniff', 'else'}
# ... (rest of your operator sets are fine) ...
arithmetic_operators = {'+', '-', '*', '/', '%'}
comparison_operators = {'==', '!=', '>', '<', '>=', '<='}
logical_operators = {'&&', '||', '!'}
parentheses = {'(', ')'}
curly_braces = {'{', '}'}
separators = {',', '.'}
semicolon = ';'


# Tokenizer function
def Tokenizer(code):
    tokens = []
    # We now process the code line by line to track the line number
    for line_number, line in enumerate(code.splitlines(), 1):
        pattern = r'"(?:\\.|[^"\\])*"|[A-Za-z_]\w*|\d+|==|!=|>=|<=|&&|\|\||[+\-*/%]=?|[(){};,]|[<>]|='
        tokenized_line = re.findall(pattern, line)

        for word in tokenized_line:
            # Check for string literals
            if word.startswith('"') and word.endswith('"'):
                tokens.append(Token(Tokens.STRING_LITERAL, word[1:-1], line_number))
            
            # Check for keywords
            elif word in keywords:
                tokens.append(Token(Tokens.KEYWORD, word, line_number))

            # Check for identifiers
            elif word.isidentifier():
                tokens.append(Token(Tokens.IDENTIFIER, word, line_number))

            # ... (the rest of your elif checks are the same, just add line_number) ...
            
            # Check for assignment operator
            elif word == '=':
                tokens.append(Token(Tokens.ASSIGNMENT_OP, word, line_number))
            # Check for literals (numbers)
            elif word.isdigit():
                tokens.append(Token(Tokens.INT_LITERAL, word, line_number))
            # Check for arithmetic operators
            elif word in arithmetic_operators:
                tokens.append(Token(Tokens.ARITHMETIC_OP, word, line_number))
            # Check for comparison operators
            elif word in comparison_operators:
                tokens.append(Token(Tokens.COMPARISON_OP, word, line_number))
            # Check for logical operators
            elif word in logical_operators:
                tokens.append(Token(Tokens.LOGICAL_OP, word, line_number))
            # Check for parentheses
            elif word in parentheses:
                tokens.append(Token(Tokens.PARENTHESIS, word, line_number))
            # Check for curly braces
            elif word in curly_braces:
                tokens.append(Token(Tokens.CURLY_BRACE, word, line_number))
            # Check for separators like comma, period
            elif word in separators:
                tokens.append(Token(Tokens.SEPARATOR, word, line_number))
            # Check for semicolon
            elif word == semicolon:
                tokens.append(Token(Tokens.SEMICOLON, word, line_number))

            # THIS IS THE KEY CHANGE
            else:
                # Instead of printing, we now raise the custom error
                raise DogLangSyntaxError(
                    f"Syntax Error: Unknown keyword '{word}' at line {line_number}"
                )
    return tokens

