def se():
    s1 = set()
    for i in range(5):
        a = input("Enter the name:")
        s1.add(a)
    print(s1)

    for i in range(2):
        b=input("Enter the name to remove:")
        s1.discard(b)
    print(s1)

    c=input("Enter the name to replace:")
    d=input("Enter the name to replace with:")
    s1.discard(c)
    s1.add(d)
    print(s1)
se()