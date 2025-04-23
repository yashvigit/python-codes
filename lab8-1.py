def q1():
    words=[]
    s=set()
    x=int(input("Enter the number of words you want to enter in list:"))
    for i in range(x):
        word=input("Enter the word:")
        words.append(word.upper())
    s=set(words)
    print(s)
q1()















# def faltu():
#     l1=['a','b','c','d']
#     s1=set()
#     for i in l1:
#         i.upper()
#     print(l1)
#     s1.add(set(l1))
#     print(s1)

# faltu()