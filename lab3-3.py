def str():
    s=input('enter any string: ')
    a=input('enter other string to serch: ')
    c=0
    if a in s:
        c+=1
    if c>0:
        print(a,'is in string',s)
    else:
        print(a,'not in',s)

str()