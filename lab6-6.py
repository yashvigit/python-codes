# t=(1,2,3,4)
# l=list(t)
# l.remove(3)
# t=tuple(l)
# print(t)


def q6():
    t=(1,2,3,5,6,7)
    t=list(t)
    t[0]=0
    t=tuple(t)
    print(t)

q6()