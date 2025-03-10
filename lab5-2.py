import random
def q2():
    lst=[]
    for i in range(20):
        lst.append(random.randint(1,10))
    print(lst)
    inp=int(input("write number between 1-9 to find occurence:"))
    for j in range(10):
        if lst[j]==inp:
            print(j)
q2()