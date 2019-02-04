#coding:utf-8

from datetime import date

now = date.today()
now_str = now.isoformat()

with open("today.txt", "wt") as outfile:
    outfile.write(now_str)

print(now_str)