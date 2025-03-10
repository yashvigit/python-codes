l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]
for i in l1:
    l2.append(i) if i not in l2 else l2# aiya else vadu na aave
#     if i not in l2:
#         l2.append(i)

print(l2)