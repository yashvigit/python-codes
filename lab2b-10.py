def check():
    x=int(input("lenght of rectangle is:"))
    y=int(input("bredth of rectangle is:"))
    a=x*y
    p=2*(x+y)
    if a>p:
        print("area of rectangle is greater than it's perimeter")
    else:
        print("area of rectangle is not greater than it's perimeter")
check()
