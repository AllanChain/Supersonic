import colors


def peer(index):
    num=input('What in %d? '%index)
    while not(num.isdigit() and 1<=int(num)<=13):
        num=input(colors.RED+'What fuck in %d? '%index+colors.NORMAL)
    return(int(num))
