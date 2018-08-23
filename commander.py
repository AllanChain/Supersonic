import card_there,card_random
import colors

def main(mode='1'):
    if mode=='1':
        peer=card_there.peer
    else:
        peer=card_random.peer
    operation=0
    #谁在几号
    known={}
    exposed=[0 for i in range(13)]
    max_expose=0
    for i in range(13):
        operation+=1
        result=peer(i)
        known[result]=i
        if result==max_expose+1:
            max_expose+=1
            exposed[i]=result
            print('expose {} at position {}'.format(result,i))
            while max_expose+1 in known:
                operation+=1
                max_expose+=1
                exposed[known[max_expose]]=max_expose
                print(colors.YELLOW+'expose {} at position {}'.format(max_expose,known[max_expose])+colors.NORMAL,end='')
                if mode=='1':
                    input()
                else:
                    print()
        else:
            print('peer {} at position {}'.format(result,i))
        print(exposed)
        print(max_expose)
    print(operation)
if __name__=='__main__':
    main(input('mode? '))
    #main(0)
