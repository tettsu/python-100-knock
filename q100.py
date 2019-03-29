#coding:utf-8

def double_substring(line):

    s = []
    
    for i in range(len(line)-1):
        for j in range(i+1,len(line)+1):
            if line[i:j] in line[j:]:
                s.append(len(line[i:j]))

    if len(s)>0 :
        return print(max(s))
    else :
        return print('無いよ')

double_substring('aaaaaa')
double_substring('abcdefg')