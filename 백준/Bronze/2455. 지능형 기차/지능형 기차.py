p=[]
a1, a2=map(int, input().split())
b1, b2=map(int, input().split())
c1, c2=map(int, input().split())
d1, d2=map(int, input().split())
a=a2
b=a-b1+b2
c=b-c1+c2
p.append(a)
p.append(b)
p.append(c)
print(max(p))