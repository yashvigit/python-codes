#check if all pts lie on st line
def collinear():
    x1=int(input("enter x1 : "))
    x2=int(input("enter x2 : "))
    x3=int(input("enter x3 : "))
    y1=int(input("enter y1 : "))
    y2=int(input("enter y2 : "))
    y3=int(input("enter y3 : "))
    if((y2-y1) * (x3-x2) == (y3-y2) * (x2-x1)):
        print("they are collinear")
    else:
        print("they are not collinear")    
collinear()


    
    
collinear()