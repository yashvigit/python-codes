def find():
    a=input("write anything:")
    count=0
    alpbt=0
    for i in a :
        if i in '0123456789':
            count+=1
    print(count)
    
    for i in a:
        if 'a'<=i<='z' or 'A'<=i<='Z':
            alpbt+=1
    print(alpbt)

find()
        
