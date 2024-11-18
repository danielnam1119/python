s=int(input())
for i in range(s):
    r, p=input().split()
    r=int(r)
    l=[]
    for j in range(len(p)):
        l.append(p[j]*r)
    print("".join(l))