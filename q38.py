#coding:utf-8

class Elements:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return("name: %s, symbol: %s, number: %s" % (self.name, self.symbol, self.number))

el_dict = {"name": "Hydrogem", "symbol": "H", "number": 1}

hydrogem = Elements(**el_dict)
print(hydrogem)
