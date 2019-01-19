# coding:utf-8

def j_hash(n):
    s = str(n)
    array = list(map(int, list(s)))
    a = sum(array)
    if n % a == 0:
        print("hashnumber")
    else:
        print("not hashnumber")

j_hash(444)