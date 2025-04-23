def names():
    s1=set()
    s1.update(['a','b','c','d','f'])
    s1.remove('f')
    s1.remove('d')
    l1=list(s1)
    l1[0]='A'
    s2=set(l1)
    print(s2)

names()
    