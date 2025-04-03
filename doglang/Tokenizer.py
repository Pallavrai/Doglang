import re


class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"\nToken({self.token_type}, '{self.value}')"


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


keywords = {'bark','wagtail','fetch','sniff','else'}


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


    pattern = r'"(?:\\.|[^"\\])*"|[A-Za-z_]\w*|\d+|==|!=|>=|<=|&&|\|\||[+\-*/%]=?|[(){};,]|[<>]|='
    tokenized_code = re.findall(pattern, code)

    for word in tokenized_code:
        # Check for string literals
        if word.startswith('"') and word.endswith('"'):
            tokens.append(Token(Tokens.STRING_LITERAL, word[1:-1]))  # Remove the quotes
        
        # Check for keywords
        elif word in keywords:
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


        else:
            print(f"Unrecognized token: {word}")


    return tokens

