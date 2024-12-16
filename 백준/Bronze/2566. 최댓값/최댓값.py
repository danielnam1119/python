n=[]
for i in range(9):
    a=list(map(int, input().split()))
    n.append(a)
x=0
y=[0,0]
for j in range(9):
    for k in range(9):
        if x<n[j][k]:
            x=n[j][k]
            y[0]=j
            y[1]=k
print(x)
print(y[0]+1,y[1]+1)