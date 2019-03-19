#coding:utf-8

# from itertools import combinations
# import random

def count_n(n_list):
    counts = []
    for n in n_list:
        count = 0
        while n % 2 == 0:
            count += 1
            n = n / 2
        else:
            counts.append(count)
            aws = min(counts)
            print(aws)

print(count_n([16,16,4]))