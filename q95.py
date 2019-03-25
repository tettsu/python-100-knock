#coding:utf-8

from datetime import date, timedelta

def check_date(today):
    Y, M, D = [int(n) for n in today.split('/')]
    dt = date(Y, M, D)
    while True:
        if Y % M == 0 and (Y / M) % D == 0:
            break
        dt += timedelta(days=1)
        Y = dt.year
        M = dt.month
        D = dt.day

    print(dt.strftime('%Y/%m/%d'))

check_date("2019/03/25")