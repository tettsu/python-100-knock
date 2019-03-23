#coding:utf-8

ans = set([])
l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    while i % 2 == 0:
        i = i // 2

    ans.add(i)

    print(len(ans))