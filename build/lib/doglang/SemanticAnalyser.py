from doglang.SymbolTable import SymbolTable
from doglang.SyntaxAnalyser import AST, SyntaxAnalyser
from doglang.Tokenizer import Tokenizer

class SemanticAnalyser:
    def __init__(self,ast:AST):
        ## first check for declaration of variables
        self.symbol_table = SymbolTable()
        self.traverseAST("assignment", ast)
      
        
    def traverseAST(self, target:str, node:AST):
        if node is None:
            return
        if node.type == target:
            self.check(node)
        for child in node.children:
            self.traverseAST(target, child)
        
    def check(self, node:AST):
        
        # node is assignment
        expression=""
        expression_type=node.children[1]
        for element in expression_type.children: ## children[0] is expression then accessing children of expression
            if element.type == "INT_LITERAL" or element.type == "ARITHMETIC_OP":
                expression += element.value
            elif element.type == "IDENTIFIER":
                if self.symbol_table.lookup(element.value) is None:
                    raise Exception("Variable not declared")
                else:
                    expression += str(self.symbol_table.lookup(element.value).value)

        result = eval(expression)
        if self.symbol_table.lookup(node.children[0].value) is None:
            self.symbol_table.insert(name=node.children[0].value,type="int",scope="local", value = result)
        else:
            self.symbol_table.modify(node.children[0].value,result)
        # if node.type == "print":
        #     if node.children[0].type == "IDENTIFIER":
        #         st=SymbolTable()
        #         if st.lookup(node.children[0].value) is None:
        #             raise Exception("Variable not declared")


# code = """  a=23+2
#             wagtail(a<1){ 
#                 bark(a)
#                 a=a+10
#             }
#             """
#     # code = """a=(10+2);
#     #           y=22;
#     #         """
# tokens=Tokenizer(code)
# # print(tokens)
# parse=SyntaxAnalyser(tokens)
# ast=parse.parse()
# semantic = SemanticCheck(ast)
 
# print(ast)

# st=SymbolTable()
# print(st.lookup("a").value)
