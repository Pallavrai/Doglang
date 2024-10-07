from Tokenizer import *
from SymbolTable import SymbolTable

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
            Error(f"Unexpected end of input. Expected {expected_type}")
        if token.token_type != expected_type or (expected_value is not None and token.value != expected_value):
            # Error(f"Expected {expected_type},{expected_value} but got {token}")
            pass
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
        
        node.addchild(self.expressions(id))
        return node
    def expressions(self,id):
        node=AST("expression")
        token=self.current_element()
        if token.token_type == Tokens.INT_LITERAL:
            literal=self.current_element() #To get value going to identifier
            value=int(literal.value)
            self.match(Tokens.INT_LITERAL) #number
            node.addchild(AST(literal.token_type,value))
            op_token=self.current_element()
            if op_token.token_type==Tokens.ARITHMETIC_OP and op_token.value == '+':  # a + b
                self.match(Tokens.ASSIGNMENT_OP,'+')
                
                node.addchild(AST(Tokens.ARITHMETIC_OP,'+'))
                operand2=self.current_element()
                node.addchild(AST(operand2.token_type,operand2.value))
                self.match(Tokens.INT_LITERAL)
                value += int(operand2.value)              
            # node.addchild(AST(literal.token_type,literal.value))
                self.insert(name=id,type="int",scope="local",value=value)
            return node


    def print_stmt(self):
        node=AST("print")
        self.match(Tokens.KEYWORD,'bark') #bark keyword
        self.match(Tokens.PARENTHESIS,'(') #( match
        token=self.current_element()
        if token.token_type == Tokens.IDENTIFIER:
            #add symbol table lookup here.
            self.match(Tokens.IDENTIFIER)
            node.addchild(AST(token.token_type,token.value))
        elif token.token_type==Tokens.INT_LITERAL:
            self.match(Tokens.INT_LITERAL)
            node.addchild(AST(token.token_type,token.value))
        else: Error("Invalid Data")
        self.match(Tokens.PARENTHESIS,')')

        return node

    



if __name__ == "__main__":
    code = "x=4+3 y=34+23 bark(x)"
    tokens=Tokenizer(code)
    # print(tokens)
    parse=SyntaxAnalyser(tokens)
    ast=parse.parse()    
    # print(ast)
    st=SymbolTable()
    print(st.lookup("y").value)
    



    