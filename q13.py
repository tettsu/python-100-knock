#coding:utf-8

import sys

args = sys.argv

def convert(text):
    if text[-1] == "C":
        cel = int(text[:-1]) #文字列の最後の文字を除外して数値にする
        aws = cel * (9/5) + 32
    elif text[-1] == "F":
        fah = int(text[:-1]) #文字列の最後の文字を除外して数値にする
        aws = (fah -32) / (9/5)
    else:
        aws = "正しく入力しよう"
    return aws

print(convert(args[1]))