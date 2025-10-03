class Symbol:
    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        self.value = value

class SymbolTable:
    def __init__(self):
        self._symbols = {}

    def insert(self, name, type, value=None):
        self._symbols[name] = Symbol(name, type, value)

    def lookup(self, name):
        return self._symbols.get(name)

    def modify(self, name, value):
        symbol = self.lookup(name)
        if symbol:
            symbol.value = value