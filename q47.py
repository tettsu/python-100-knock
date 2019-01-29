import re

sentence = "Chicken Little"

#ソースの先頭が、指定したパターンと一致しているか
m = re.match("Chi", sentence)
if m:
    print(m.group())

m1 = re.match(".*ttle", sentence)
if m1:
    print(m1.group())

m2 = re.search("ttle", sentence)
if m2:
    print(m2.group())

m3 = re.findall("n", sentence)
print(len(m3))

m4 = re.findall("n.", sentence)

m5 = re.findall("n.?", sentence)
