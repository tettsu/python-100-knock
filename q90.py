from numpy import random

def num_fight(card_number):
    cards = list(range(card_number))
    count = 0
    alice_cards = []
    bob_cards = []

    while len(cards) != 0:
        taken_card = max(cards)
        cards.remove(taken_card)
        count += 1

        if count % 2 == 1:
            alice_cards.append(taken_card)
        else:
            bob_cards.append(taken_card)

    alice_score = sum(alice_cards)
    bob_score = sum(bob_cards)

    aws = alice_score - bob_score
    
    print(aws)

num_fight(100)