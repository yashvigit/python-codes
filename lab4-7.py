import math
def ncrnpr():
    n=int(input("enter any no.: "))
    r=int(input("enter some common difference: "))
    print("permutation: ",(math.factorial(n)/math.factorial(n-r)))
    print("combination: ",math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

ncrnpr()
