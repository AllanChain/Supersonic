from random import shuffle
_cards=list(range(1,13+1))
shuffle(_cards)
def peer(index):
    return _cards[index]
def conservative():
    step=25
    x=1
    while _cards.index(x+1)>_cards.index(x):
        step-=1
        x+=1
    return step
def rerand():
    shuffle(_cards)
