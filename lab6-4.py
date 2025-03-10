l=[('jalebi',80),('kaju-katli',50),('mohanthal',100)]
for i in range(2):
    for j in range(2):
        if l[i][1]<l[j][1]:
            l[i],l[j]=l[j],l[i]
print(l)       




# import operator
# def q4():
#     l=[('Alloo',100),('Burger',120),('pizza',200)]
#     lst=sorted(l,key=operator.itemgetter(1),reverse=True)
#     print(lst)
    
# q4()   
    
    