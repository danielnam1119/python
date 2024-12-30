n, k=map(int, input().split())
value=[]
for i in range(n):
    r=n%(i+1)
    if r==0:
        value.append(n//(i+1))
value.sort()
if len(value)>(k-1):
    print(value[k-1])
else:
    print(0)