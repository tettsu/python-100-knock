#coding:utf-8

import time
from datetime import date

now = date.today()
now_str = now.isoformat() #文字列の形にする

fmt = '%Y-%m-%d'
now_str = time.strptime(now_str, fmt)

print(now_str)