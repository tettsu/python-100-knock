#coding:utf-8

#英字(小文字＆大文字) :string.ascii_letters
#数字:string.digits
#string.punctuation

import string
import random

a = ''.join(
    [random.choice(string.ascii_letters + string.digits) for i in range(8)]
    )

print(a)