from doglang.SymbolTable import SymbolTable
from doglang.SyntaxAnalyser import AST, SyntaxAnalyser
from doglang.Tokenizer import Tokenizer
from doglang.ExpressionParser import parse_and_evaluate

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
        expression_type = node.children[1]
        
        # Use the new expression parser instead of eval
        try:
            result = parse_and_evaluate(expression_type.children, self.symbol_table)
        except Exception as e:
            raise Exception(f"Error evaluating expression in semantic analysis: {str(e)}")
        
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
