from Tokenizer import Tokens, Tokenizer
from SymbolTable import SymbolTable
from evaluator import *

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
            Error(f"Expected {expected_type},{expected_value} but got {token}")
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
        elif token.token_type == Tokens.KEYWORD and token.value=='wagtail':
            return self.loop_stmt()
        else:
            Error("Unexpected Token.")

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
        node.addchild(self.expressions(id))
        if self.lookup(id):
            self.modify(id,self.expressions(id))

        return node
    
    def expressions(self,id=None):
        node=AST("expression")
        token=self.current_element()
        
        if token.token_type == Tokens.INT_LITERAL or token.token_type == Tokens.PARENTHESIS or token.token_type == Tokens.IDENTIFIER:
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

    



if __name__ == "__main__":
    code = """a=0;
              bark("Hello");
              wagtail(a<10){
                  a=a+1;
              }

        
            """
    # code = """a=(10+2);
    #           y=22;
    #         """
    tokens=Tokenizer(code)
    # print(tokens)
    parse=SyntaxAnalyser(tokens)
    ast=parse.parse()    
    print(ast)
    # st=SymbolTable()
    # print(st.lookup("a").value)
    # print(st.lookup("y").value)
    
    



    