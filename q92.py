#coding:utf-8

def remocon(a,b):
    target = b - a
    min_count = 100
    for o in range(100):
        for f in range(100):
            for t in range(100):
                if o + 5 * f + 10 * t == target or -1 * o + -5 * f + -10 * t == target:
                    count = o + t + f
                    if min_count > count:
                        min_count = count
                        a_o = o
                        a_f = f
                        a_t = t
    
    print(a_o,a_f,a_t)

remocon(10,5)
