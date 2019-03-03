def second_index(text, symbol):
    count = 0
    for i in range(len(text)):
        if text[i] == symbol:
            count += 1
            if count == 2:
                return i
    return None

second_index("I am a good student but you are not a good student", "g")