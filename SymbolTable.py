"""Symbol Table(name,type,scope,value)"""
symbols=[]
class SymbolTable:
    def __init__(self,name="",type="",scope="",value=""):
        self.name=name
        self.type=type
        self.scope=scope
        self.value=value

    def insert(self,name,type,scope,value):
        symbols.append(SymbolTable(name,type,scope,value))
    
    def lookup(self,name):
        for entry in symbols:
            if entry.name==name:
                return entry
        return None
    
    def modify(self,name,value):
        for entry in symbols:
            if entry.name==name:
                entry.value=value
                return
        return None