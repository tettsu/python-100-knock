import random

#coding:utf-8
def randomList(size,lower,upper):
    list = []
    for i in range(size):
        list.append(random.randint(lower,upper))
    print(list)

randomList(10,30,90)
