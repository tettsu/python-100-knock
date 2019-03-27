#coding:utf-8

from datetime import date, timedelta

def perfect_number(n):
    y_num = []

    for i in range(2,n):
        if n % i == 0:
            y_num.append(i)
            m = n // i
            y_num.append(m)
    y_num.append(1)
    y_num = set(y_num)
    sum_y = sum(y_num)
    if sum_y == n:
        print("完全数だ！")
    else:
        print("完全数ではありません")

perfect_number(28)