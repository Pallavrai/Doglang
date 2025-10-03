"""Symbol Table(name,type,scope,value)"""
# symbols=[]
class SymbolTable:
    def __init__(self):
        # self.name=name
        # self.type=type
        # self.scope=scope
        # self.value=value
        self.symbols=[]

    def insert(self,name="",type="",scope="",value=""):
        
        entry = {
            'name':name,
            'type':type, 
            'scope':scope,
            'value':value
        }
        self.symbols.append(entry)
    
    def lookup(self,name):
        for entry in self.symbols:
            if entry['name']==name:
                return entry
        return None
    
    def modify(self,name,value):
        for entry in self.symbols:
            if entry['name']==name:
                entry['value'] = value
                return
        return None
    
    def __repr__(self):
        if not self.symbols:
            return "Symbol Table is empty"

        result=""
        for entry in self.symbols:
            result += f" name : {entry['name']} | value : {entry["value"]} | type : {entry['type']} | scope : {entry['scope']}\n"
        return result