"""Symbol Table(name,type,scope,value)"""

class SymbolTable:
    # __init__ creates an instance-specific list.
    def __init__(self):
        self.symbols=[]

    def insert(self,name,type,scope,value):

        symbol_entry = {'name': name, 'type': type, 'scope': scope, 'value': value}
        self.symbols.append(symbol_entry)
    
    def lookup(self,name):
        for entry in self.symbols:
            if entry['name']==name:
                return entry     # Returns the dictionary
        return None
    
    # modifies the instance list.
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
            result += f" name : {entry['name']} | value : {entry['value']} | type : {entry['type']} | scope : {entry['scope']}\n"
        return result