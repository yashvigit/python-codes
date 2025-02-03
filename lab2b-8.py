def check():
    a=int(input("first angle is:"))
    b=int(input("second angle is:"))
    c=int(input("third angle is:"))
    if a+b+c==180:
        print("triangle is valid")
    else:
        print("triangle is not valid")
check()
