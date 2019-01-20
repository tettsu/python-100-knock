#coding:utf-8

def pocket(aim):
    count = 0
    biskets = 1
    while biskets < aim:
        count += 1
        biskets = 2 ** count 
    else:
        print("{}回ポケットをたたいてください".format(count))

pocket(10)