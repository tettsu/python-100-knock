#coding:utf-8

from itertools import combinations

strr = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

strr = strr.replace('.',"")
print(strr)
strr = strr.replace(',',"")
print(strr)
strr = strr.split()
print(strr)

a_list = []

for word in strr:
    a_list.append(len(word))

print(a_list)