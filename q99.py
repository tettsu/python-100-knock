#coding:utf-8

def convert_10(str_number, radix):
    try:
        return print(int(str_number, radix))
    except ValueError:
        return -1

convert_10('3C5',16)