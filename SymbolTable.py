#Taylor Gray

class SymbolTable:
    def __init__(self):
        self.table = dict()

    def addEntry(self, symbol, address):
        self.table[symbol] = address
    
    def contains(self, symbol):
        return symbol in self.table
    
    def GetAddress(self, symbol):
        return self.table[symbol]