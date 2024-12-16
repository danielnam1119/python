n, m=map(int, input().split())
a=[]
b=[]
for row in range(n):
    k=list(map(int, input().split()))
    a.append(k)
for row in range(n):
    p=list(map(int, input().split()))
    b.append(p)
for row in range(n):
    for col in range(m):
        print(a[row][col]+b[row][col], end=" ")
    print()