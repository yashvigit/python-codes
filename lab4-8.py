def facto():
    n=int(input("enter any no.: "))
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
facto()