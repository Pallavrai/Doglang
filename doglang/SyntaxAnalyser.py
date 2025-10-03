from doglang.Tokenizer import Tokens
from doglang.SymbolTable import SymbolTable
# Import the custom exception we created in error.py
from doglang.error import DogLangSyntaxError

class AST:
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
    
    # Add a 'peek' method to look at the next token without consuming it
    def peek(self):
        if self.current + 1 < len(self.token):
            return self.token[self.current + 1]
        return None
    
    def match(self,expected_type,expected_value=None):
        token=self.current_element()
        if not token:
            raise DogLangSyntaxError(f"Unexpected end of input. Expected {expected_type}")
        if token.token_type != expected_type or (expected_value is not None and token.value != expected_value):
            # Use the new error class and include the line number
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
    
    # --- THIS IS THE KEY CHANGE ---
    def statement(self):
        token=self.current_element()
        
        if token.token_type == Tokens.KEYWORD:
            if token.value=='bark':
                return self.print_stmt()
            elif token.value=='wagtail':
                return self.loop_stmt()
            elif token.value=='sniff':
                return self.conditional_statement()
        
        elif token.token_type == Tokens.IDENTIFIER:
            # Look ahead to see if the next token is an assignment operator
            next_token = self.peek()
            if next_token and next_token.token_type == Tokens.ASSIGNMENT_OP:
                return self.assignment()
            else:
                # If it's an identifier NOT followed by '=', it's an unknown keyword
                raise DogLangSyntaxError(f"Syntax Error: Unknown keyword '{token.value}' at line {token.line}")

        # If we reach here, the token is not a valid start to a statement
        raise DogLangSyntaxError(f"Unexpected token '{token.value}' at line {token.line}")

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
        id = self.current_element().value
        node.addchild(AST(Tokens.IDENTIFIER,id))
        self.match(Tokens.IDENTIFIER)
        self.match(Tokens.ASSIGNMENT_OP,'=')
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
                return node # Return early for fetch expression

        node=AST("expression")
        while self.current_element() and self.current_element().value != ';':
            if self.current_element().token_type == Tokens.CURLY_BRACE: 
                return node
            node.addchild(AST(self.current_element().token_type,self.current_element().value))
            self.increment()
        
        # Consume the semicolon if it exists
        if self.current_element() and self.current_element().value == ';':
            self.increment()
        
        return node

    def print_stmt(self):
        node=AST("print")
        self.match(Tokens.KEYWORD,'bark') #bark keyword
        node.addchild(self.expressions())
        return node
