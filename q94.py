#coding:utf-8

def substract_game(n, ng_words):
    count = 0
    flag = 0
    a = ng_words[0]
    b = ng_words[1]
    c = ng_words[2]
    
    while count < 100 and n != (a or b or c) and n >= 4:
        if not (n-3 in ng_words):
            count += 1
            n = n - 3
        elif not (n-2 in ng_words):
            count += 1
            n = n - 2
        elif not (n-1 in ng_words):
            count += 1
            n = n - 1
        else:
            flag = 0
            break

    if (n == 1 or n == 2 or n == 3) and count <= 99:
        n = 0
        flag = 1

    if n > 0:
        flag = 0

    if flag == 1:
        print("yes")
    else:
        print("no")

substract_game(100,[24,55,92])
        