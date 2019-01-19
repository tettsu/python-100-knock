# coding:utf-8

#最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a = 16
b = 6
xab = gcd(a,b)
print(xab)

#最小公倍数
zab = a*b/xab
print(zab)