#coding:utf-8

e2f = {"dog":"chien", "cat":"chat", "walrus":"mourse"}
print(e2f)

print(e2f["walrus"])

f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)

print(set(e2f.keys()))