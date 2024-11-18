basket=[]
n, m=map(int, input().split())
for j in range(1, n+1):
    basket.append(j)
for i in range(m):
    a, b=map(int, input().split())
    temp=basket[a-1:b]
    temp.reverse()
    basket[a-1:b]=temp
print(*basket)