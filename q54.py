#text1
test1 = "This is a test of the emergency text system"

outfile = open("test.txt", "wt")
outfile.write(test1)
outfile.close()

#withを使うとclose呼び出しを避けることができる
with open("test.txt", "wt") as outfile:
    outfile.write(test1)