#coding:utf-8

import binascii
#文字列 -> 16進数
print(binascii.hexlify(b'Hello'))

#16進数 -> 文字列
print(binascii.unhexlify('48656c6c6f'))
