def flatten(ls):
    r = []
    for i in ls:
        if type(i) is list:
            r.extend(flatten(i))
        else:
            r.append(i)
    return r

lis_a = [[1,2],3,4,5,[6,[7,[8,9]]]]
print(flatten(lis_a))