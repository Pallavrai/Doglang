from Tokenizer import *


class AST:
    def __init__(self,type,value=None):
        self.type=type
        self.value=value
        self.children=[]
    
    def addchild(self,child):
        self.children.append(child)
    
    def __repr__(self) -> str:
        return f'AST({self.type},{self.value},{self.children})'

class Error:
    def __init__(self,error):
        raise Exception(f'Syntax Error: {error}')

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
    
    def match(self,expected_type,expected_value=None):
        token=self.current_element()
        if not token:
            self.error(f"Unexpected end of input. Expected {expected_type}")
        if token.token_type != expected_type or (expected_value is not None and token.value != expected_value):
            self.error(f"Expected {expected_type} but got {token}")
        self.increment()
        return token
            

    #Grammar rules

    def parse(self):
        return self.program()
    def program(self):
        node=AST("Program")
        while self.current<len(self.token):
            node.addchild(self.statement())
        return node
    
    def statement(self):
        token=self.current_element()
        
        if token.token_type == Tokens.KEYWORD and token.value=='bark':
            return self.print_stmt()
        elif token.token_type == Tokens.IDENTIFIER:
            return self.assignment()
        else:
            Error("Unexpected Token.")
    
    def assignment(self):
        node=AST("assignment")
        id = self.current_element().value #To get identifier name
        self.match(Tokens.IDENTIFIER) # identifier
        self.match(Tokens.ASSIGNMENT_OP,'=')  #checks for =

        value=self.current_element().value #To get value assigned to identifier
        self.match(Tokens.LITERAL) #number or string
        self.insert(id,"int","local",value)
        
    def print_stmt(self):
        node=AST("print")
        self.match(Tokens.KEYWORD,'bark') #bark keyword
        self.match(Tokens.PARENTHESIS,'(') #( match
        token=self.current_element()
        if token.token_type == Tokens.IDENTIFIER:
            #add symbol table lookup here.
            self.match(Tokens.IDENTIFIER)
            node.addchild(AST(token.token_type,token.value))
        elif token.token_type==Tokens.LITERAL:
            self.match(Tokens.LITERAL)
            node.addchild(AST(token.token_type,token.value))
        else: Error("Invalid Data")
        self.match(Tokens.PARENTHESIS,')')

        return node

    



if __name__ == "__main__":
    code = "x=456456745 bark(x)"
    tokens=Tokenizer(code)
    print(tokens)
    parse=SyntaxAnalyser(tokens)
    ast=parse.parse()    
    print(ast)
    st=SymbolTable()
    print(st.lookup("x").value)
    



    