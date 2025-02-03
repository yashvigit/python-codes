#total ,avg and result with grade 
def result():
    a=int(input("enter maths marks: "))
    b=int(input("enter physics marks: "))
    c=int(input("enter chemistry marks: "))
    total=a+b+c
    avg=total/3
    print("total marks: ",total)
    print("avg: ",avg)
    if(a<=39 or b<=39 or c<=39):
        print("result:fail")
    else:
        print("result:pass")  
    for marks in [a,b,c]:
        if(marks<=39):
            grade= 'F'
        elif(40<=marks<=44):
            grade='P'
        elif(45<=marks<=49):
            grade='C'
        elif(50<=marks<=54):
            grade='B'
        elif(55<=marks<=59):
            grade='B+'
        elif(60<=marks<=69):
            grade='A'
        elif(70<=marks<=79):
            grade='A+'
        else:
            grade='O'
        print(f"Marks:{marks} , grade:{grade}")    
result()