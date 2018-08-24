from card_random import peer,conservative,rerand

def main():
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
            while max_expose+1 in known:
                operation+=1
                max_expose+=1
                exposed[known[max_expose]]=max_expose
    return operation
if __name__=='__main__':
    total=0
    for i in range(100):
        operation=main()
        c_operation=conservative()
        delta=c_operation-operation
        total+=delta
        print('conservative {},radical {},delta {}'.format(c_operation,operation,delta))
        rerand()
    print('average {}'.format(total/(i+1)))
