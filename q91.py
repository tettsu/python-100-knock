#coding:utf-8

def count_one(n):
    counts = 0
    for i in range(1,n+1):
        str_i = str(i)
        count = str_i.count("1")
        counts += count
    return counts

print(count_one(100))