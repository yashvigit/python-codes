def check():
    a=int(input("enter a year:"))
    if a%400==0:
        if a%100==0:
            if a%4==0:
                print(a,"is a leap year")
    else:
         print(a,"is not a leap year")
check()
