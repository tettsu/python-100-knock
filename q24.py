#coding:utf-8

import string

def find_frequent_word(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

a = find_frequent_word("sfhsuif oidfhjaiosfh987809lahdlUGliosdgfdOIHDF90875iu7vcbu")
print(a)