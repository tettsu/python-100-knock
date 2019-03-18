#coding:utf-8

from itertools import combinations
import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = text.split()

result_list = []

for word in words:
    if len(word) < 4:
        print("passed!")
        pass
    else:
        char_list = list(word)
        print(char_list)

        mid_list = char_list[1:-1]
        print(mid_list)

        random.shuffle(mid_list)
        print(mid_list)

        word = word[0] + "".join(mid_list) + word[-1]
        print(word)
    result_list.append(word)

result_str = " ".join(result_list)
print(result_str)