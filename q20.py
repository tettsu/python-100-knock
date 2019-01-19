#coding:utf-8

def check_hand(a,b,c,d,e):
    list_hands = [a,b,c,d,e]
    dict_hands = {0 : "NO PAIR", 1 : "ONE PAIR", 2 : "TWO PAIR", 3 : "THREE_CARD", 4 : "FOUR CARD", 5 : "FULL HOUSE"}
    results = []

    for i in list_hands:
        count_i = list_hands.count(i)
        for j in list_hands:
            count_j = list_hands.count(j)

            if count_i == 2 and count_j < 2:
                results.append(1)

            if count_i == 2 and count_j == 2:
                results.append(2)

            if count_i == 3 and count_j == 1:
                results.append(3)

            if count_i == 4 and count_j == 1:
                results.append(4)

            if count_i == 3 and count_j == 2:
                results.append(5)
            else:
                results.append(0)

    result = max(results)
    return dict_hands[result]

print(check_hand(1,1,7,1,3))