def fibb():
    ā=0
    b=int(input("enter numbers in a series: "))
    c=int(input("enter first element of a series: "))
    d=int(input("enter second element of a series: "))
    for i in range(b):
        a=c+d
        print(a)
        c,d=d,a
fibb()