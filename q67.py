#coding:utf-8

from datetime import timedelta
from datetime import date
my_time = date(1988, 6, 24)

my_future = my_time + timedelta(days=10000)

print(my_future)

