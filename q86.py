#coding:utf-8

from itertools import combinations

str1 = 'パトカー'
str2 = 'タクシー'
strzip = zip(str1,str2)
print(strzip)

strchukan = [a + b for a, b in strzip]

print(''.join(strchukan))






strgattai = [str1,str2]
print('と'.join(strgattai))