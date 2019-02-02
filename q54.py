<<<<<<< HEAD
#text1
test1 = "This is a test of the emergency text system"

outfile = open("test.txt", "wt")
outfile.write(test1)
outfile.close()

#withを使うとclose呼び出しを避けることができる
with open("test.txt", "wt") as outfile:
=======
#coding:utf-8

test1 = "This is a test of the emergency text system."

outfile = open("test.txt", "wt")
outfile.write(test1)
outfile.close

with open("test.txt", "wt") as outfiles:
>>>>>>> 552381dfe053bf28484908c776f10f6f8f17524e
    outfile.write(test1)