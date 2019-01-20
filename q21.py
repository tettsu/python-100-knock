#coding:utf-8

def cal_pattern(a,b,c,x):
        count = 0
        for i in range(a + 1):
            for j in range (b + 1):
                for k in range ( c + 1 ):
                    if 500 * i + 100 * j + 50 * k == x:
                        count += 1
        return count

print(cal_pattern(3,5,6,1500))
