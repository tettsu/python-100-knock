#coding:utf-8

def long_repeat(line):
    if line == '':
        return(0)
    else:
        count=1
        count_chr=[1]
        for i in range(1,len(line)):
            if line[i-1] == line[i]:
                count += 1
            else:
                count = 1
            count_chr.append(count)
        return max(count_chr)
    

print(long_repeat("dsfiohdoidasdgiasd89ssssss8970sadaskdsa"))