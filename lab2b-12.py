#check position of point wrt circle 
import math
def position():
    h = float(input("Enter the x-coordinate of the circle's center: "))
    k = float(input("Enter the y-coordinate of the circle's center: "))
    r = float(input("Enter the radius of the circle: "))
    x = float(input("Enter the x-coordinate of the point: "))
    y = float(input("Enter the y-coordinate of the point: "))
    distance = math.sqrt(math.pow(x - h, 2) + math.pow(y - k, 2))
    if distance < r:
        print("The point lies inside the circle.")
    elif distance == r:
        print("The point lies on the circle.")
    else:
        print("The point lies outside the circle.")
position()
