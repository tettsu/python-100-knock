#coding:utf-8

hex_str = '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'

import binascii
gif = binascii.unhexlify(hex_str)
print(gif[:6] == b'GIF89a')
