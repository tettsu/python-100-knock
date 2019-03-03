def popular_words(text: str, words: list) -> dict:
    text = text.lower().split()
    count_list = []
    for word in words:
        count = text.count(word)
        count_list.append(count)
    aws = dict(zip(words, count_list))
    return aws