data=[]
for i in range(9):
    a=int(input())
    data.append(a)
print(max(data))
print(data.index(max(data))+1)