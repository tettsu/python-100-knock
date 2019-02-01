#coding:utf-8

test1 = "This is a test of the emergency text system."

outfile = open("test.txt", "wt")
outfile.write(test1)
outfile.close

with open("test.txt", "wt") as outfiles:
    outfile.write(test1)