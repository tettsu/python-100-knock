def safe_pawns(pawns):
    pwans = list(pawns)
    cols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    s_pwans = []
    for i in pawns:
        target = []
        for j in pwans:
            if int(i[1])+1 == int(j[1]):
                target.append(j)
        for k in target:
            if abs(cols.get(k[0]) - cols.get(i[0])) == 1:
                s_pwans.append(k)
                if s_pwans.count(k) > 1:
                    s_pwans.pop()
    return len(s_pwans)

aws = {"b4","c4","d4","e4","f4","g4","e3"}
safe_pawns(aws)