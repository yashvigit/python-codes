def differ():
    s1={'aditi','arya','bhavi','bhavana'}
    sa=set()
    sb=set()
    for i in s1:
        if i.startswith('a'):
            sa.add(i)
    print("names that starts with a:",sa)

    for i in s1:
        if i.startswith("b"):
            sb.add(i)
    print("names that starts with b:",sb)

differ()
