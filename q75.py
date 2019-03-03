#coding:utf-8

def first_word(text: str) -> str:
    if text.find(",")>= 0:
        text2= text.replace(',', ' ')
    if text.find(".")>=0:
        text2=text.replace('.', ' ')
    texts = text2.split()
    return texts[0]

first_word("..... greetings, friends")