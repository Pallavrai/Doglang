from doglang.Tokenizer import Tokens, Tokenizer
from doglang.SymbolTable import SymbolTable
# Import the custom exception you created
from doglang.error import DogLangSyntaxError, DogLangError

class AST:
    # ... (Your AST class is fine, no changes needed) ...
    def __init__(self,type,value=None):
        self.type=type
        self.value=value
        self.children=[]
    
    def addchild(self,child):
        self.children.append(child)
    
    def __repr__(self) -> str:
        return self._pretty_print()
    
    def _pretty_print(self, indent=0):
        result = " " * indent + f"AST({self.type}, {self.value}, ["
        
        if not self.children:
            result += "])"
            return result
            
        result += "\n"
        for child in self.children:
            result += " " * (indent + 4) + child._pretty_print(indent + 4) + ",\n"
        
        result += " " * indent + "])"
        return result


class SyntaxAnalyser(SymbolTable):
    def __init__(self,token) -> None:
        self.token=token
        self.current=0
    
    def current_element(self):
        if self.current < len(self.token):
            return self.token[self.current]
        return None
        
    def increment(self):
        self.current+=1
    
    # NEW HELPER FUNCTION to look ahead without consuming the token
    def peek(self):
        if self.current + 1 < len(self.token):
            return self.token[self.current + 1]
        return None

    def match(self,expected_type,expected_value=None):
        token=self.current_element()
        if not token:
            raise DogLangSyntaxError(f"Unexpected end of input. Expected {expected_type}")
        if token.token_type != expected_type or (expected_value is not None and token.value != expected_value):
            # Using the new error with line number for better feedback
            raise DogLangSyntaxError(f"Expected {expected_type} '{expected_value}' but got {token.token_type} '{token.value}' at line {token.line}")
        self.increment()
        return token

    #Grammar rules
    def parse(self):
        return self.program()

    def program(self):
        node=AST("Program")
        while self.current < len(self.token):
            node.addchild(self.statement())
        return node
    
    # KEY CHANGE IS HERE
    def statement(self):
        token = self.current_element()
        
        if token.token_type == Tokens.KEYWORD:
            if token.value == 'bark':
                return self.print_stmt()
            elif token.value == 'wagtail':
                return self.loop_stmt()
            elif token.value == 'sniff':
                return self.conditional_statement()
        
        elif token.token_type == Tokens.IDENTIFIER:
            # Look ahead to see if the next token is an '='
            next_token = self.peek()
            if next_token and next_token.token_type == Tokens.ASSIGNMENT_OP:
                return self.assignment()
            else:
                # This is an identifier NOT followed by '=', so it's a typo
                raise DogLangSyntaxError(f"Syntax Error: Unknown keyword '{token.value}' at line {token.line}")
        
        # If we get here, it's a token that can't start a statement
        raise DogLangSyntaxError(f"Unexpected token '{token.value}' at line {token.line}")

    # ... (rest of your file is fine) ...
    def loop_stmt(self):
        node=AST("loop")
        self.match(Tokens.KEYWORD,'wagtail')
        node.addchild(self.expressions())
        self.match(Tokens.CURLY_BRACE,'{') 
        while self.current_element().value != '}':
            node.addchild(self.statement())
        self.match(Tokens.CURLY_BRACE,'}')
        return node
    
    def assignment(self): 
        node=AST("assignment")
        id = self.current_element().value #To get identifier name
        node.addchild(AST(Tokens.IDENTIFIER,id))
        self.match(Tokens.IDENTIFIER) # identifier
        self.match(Tokens.ASSIGNMENT_OP,'=')  #checks for = 
        node.addchild(self.expressions())
        return node
    
    def code_block(self):
        node=AST("block")
        self.match(Tokens.CURLY_BRACE,'{') 
        while self.current_element().value != '}':
            node.addchild(self.statement())
        self.match(Tokens.CURLY_BRACE,'}')
        return node
    
    def conditional_statement(self):
        node=AST("conditional")
        self.match(Tokens.KEYWORD)
        node.addchild(self.expressions())
        node.addchild(self.code_block())
        if(self.current_element() and self.current_element().value == 'else'):
            node.addchild(self.else_statement())
        return node

    def else_statement(self):
        node = AST(Tokens.KEYWORD,"else")
        self.match(Tokens.KEYWORD)
        node.addchild(self.code_block())
        return node

    def expressions(self):
        token=self.current_element()
        if token.token_type == Tokens.KEYWORD:
            if token.value == "fetch":
                self.match(Tokens.KEYWORD,'fetch')
                node = AST(Tokens.KEYWORD,"input")
                node.addchild(self.expressions())
        if token.token_type == Tokens.INT_LITERAL or token.token_type == Tokens.PARENTHESIS or token.token_type == Tokens.IDENTIFIER:
            node=AST("expression")
            while self.current_element().value != ';':
                if self.current_element().token_type == Tokens.CURLY_BRACE: 
                    return node
                node.addchild(AST(self.current_element().token_type,self.current_element().value))
                self.increment()
            self.increment()
        return node

    def print_stmt(self):
        node=AST("print")
        self.match(Tokens.KEYWORD,'bark') #bark keyword
        node.addchild(self.expressions())
        return node