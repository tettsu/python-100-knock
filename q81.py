#coding:utf-8

from itertools import combinations

def twosums(x, target):
    for item in combinations(x, 2):
        if sum(item) == target:
            return item

nums = [2,7,11,15]
target = 9
print(twosums(nums, target))
