#coding:utf-8

import pprint

def checkio(number):

    ret = []

    # rangeのstepが負なら、stopより大きい最小数がゴール( 9 -> 2 となる)
    for i in range(9, 1, -1):

        # number/i を実施して余りを出す
        # 「0」は偽なので、「numberを割り切れるiの時(つまり約数の時)」だけ繰り返す
        while not number % i:
            number /= i
            ret.append(i)
            pprint.pprint(sorted(ret))
            if number == i:
                pprint.pprint(sorted(ret))
    return 0

checkio(50)
checkio(4)
