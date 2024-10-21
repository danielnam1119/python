n=int(input())
a=list(map(int,input().split()))
v=int(input())
res=0
for i in range(n):
    if a[i]==v:
        res+=1
print(res)