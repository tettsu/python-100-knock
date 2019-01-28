#coding:utf-8

class Elements:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

el_dict = {"name": "Hydrogem", "symbol": "H", "number": 1}

hydrogem = Elements(**el_dict)

print(hydrogem.name)
