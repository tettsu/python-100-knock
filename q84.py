#coding:utf-8

from itertools import combinations

def isValid(x):
    table = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for elm in x:
        if elm in table.keys():
            stack.append(table[elm])
        elif elm in table.values() and elm != stack.pop():
            return False
    return False if len(stack) else True

aaa = []
if len(aaa)==True:
    print(len(aaa))

print(isValid('[aaa]'), isValid('('), isValid('()[]{}'), isValid('(]'), isValid('([)]'), isValid('{()}'))
