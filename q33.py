#coding:utf-8

def get_odds():
    for number in range(1,10,2):
        yield number

for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print(number)
        break