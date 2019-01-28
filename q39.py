#coding:utf-8

class Elements:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    def symbol(self):
        return self.__symbol

    def number(self):
        return self.__number

el_dict = {"name": "Hydrogem", "symbol": "H", "number": 1}

hydrogem = Elements(**el_dict)

print(hydrogem.name)
