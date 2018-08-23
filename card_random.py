from random import shuffle
_cards=list(range(1,13+1))
shuffle(_cards)
def peer(index):
    return _cards[index]
