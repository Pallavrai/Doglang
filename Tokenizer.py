import re

# Define a sample Token class for demonstration
class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, '{self.value}')"

# Token categories/types
class Tokens:
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    ASSIGNMENT_OP = 'ASSIGNMENT_OP'
    LITERAL = 'LITERAL'
    #LITERALS
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

# Sample list of keywords (add more based on the language)
"""
bark -> print
wagtail -> loop

"""
keywords = {'bark','wagtail'}

# Operators and separators for various token types
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

    # Regex to match identifiers, literals, operators, parentheses, curly braces, etc.
    tokenized_code = re.findall(r'[A-Za-z_]\w*|\d+|==|!=|>=|<=|&&|\|\||[+\-*/%]=?|[(){};,]|[<>]|=', code)

    for word in tokenized_code:
        # Check for keywords
        if word in keywords:
            tokens.append(Token(Tokens.KEYWORD, word))

        # Check for identifiers
        elif word.isidentifier():
            tokens.append(Token(Tokens.IDENTIFIER, word))

        # Check for assignment operator
        elif word == '=':
            tokens.append(Token(Tokens.ASSIGNMENT_OP, word))

        # Check for literals (numbers)
        elif word.isdigit():
            tokens.append(Token(Tokens.INT_LITERAL, word))

        # Check for arithmetic operators
        elif word in arithmetic_operators:
            tokens.append(Token(Tokens.ARITHMETIC_OP, word))

        # Check for comparison operators
        elif word in comparison_operators:
            tokens.append(Token(Tokens.COMPARISON_OP, word))

        # Check for logical operators
        elif word in logical_operators:
            tokens.append(Token(Tokens.LOGICAL_OP, word))

        # Check for parentheses
        elif word in parentheses:
            tokens.append(Token(Tokens.PARENTHESIS, word))

        # Check for curly braces
        elif word in curly_braces:
            tokens.append(Token(Tokens.CURLY_BRACE, word))

        # Check for separators like comma, period
        elif word in separators:
            tokens.append(Token(Tokens.SEPARATOR, word))

        # Check for semicolon
        elif word == semicolon:
            tokens.append(Token(Tokens.SEMICOLON, word))

        # Catch unrecognized tokens
        else:
            print(f"Unrecognized token: {word}")

    # Output the list of tokens
    return tokens

if __name__ == "__main__":
    code = "x=3+4 bark(x)"
    print(Tokenizer(code))
