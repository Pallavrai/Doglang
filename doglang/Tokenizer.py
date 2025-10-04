import re
from .error import DogLangSyntaxError 


class Token:
   
    def __init__(self, token_type, value, line):
        self.token_type = token_type
        self.value = value
        self.line = line

    def __repr__(self):
       
        return f"\nToken({self.token_type}, '{self.value}', line={self.line})"


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

    # Process the code line by line to get the line number
    for line_number, line in enumerate(code.splitlines(), 1):
        pattern = r'"(?:\\.|[^"\\])*"|[A-Za-z_]\w*|\d+|==|!=|>=|<=|&&|\|\||[+\-*/%]=?|[(){};,]|[<>]|='
        tokenized_line = re.findall(pattern, line)

        for word in tokenized_line:
            # Pass the 'line_number' to every new Token instance
            if word.startswith('"') and word.endswith('"'):
                tokens.append(Token(Tokens.STRING_LITERAL, word[1:-1], line_number))
            elif word in keywords:
                tokens.append(Token(Tokens.KEYWORD, word, line_number))
            elif word.isidentifier():
                tokens.append(Token(Tokens.IDENTIFIER, word, line_number))
            elif word == '=':
                tokens.append(Token(Tokens.ASSIGNMENT_OP, word, line_number))
            elif word.isdigit():
                tokens.append(Token(Tokens.INT_LITERAL, word, line_number))
            elif word in arithmetic_operators:
                tokens.append(Token(Tokens.ARITHMETIC_OP, word, line_number))
            elif word in comparison_operators:
                tokens.append(Token(Tokens.COMPARISON_OP, word, line_number))
            elif word in logical_operators:
                tokens.append(Token(Tokens.LOGICAL_OP, word, line_number))
            elif word in parentheses:
                tokens.append(Token(Tokens.PARENTHESIS, word, line_number))
            elif word in curly_braces:
                tokens.append(Token(Tokens.CURLY_BRACE, word, line_number))
            elif word in separators:
                tokens.append(Token(Tokens.SEPARATOR, word, line_number))
            elif word == semicolon:
                tokens.append(Token(Tokens.SEMICOLON, word, line_number))
            else:
                # Raise a syntax error for unrecognized tokens
                raise DogLangSyntaxError(f"Unrecognized token '{word}' at line {line_number}")

    return tokens

