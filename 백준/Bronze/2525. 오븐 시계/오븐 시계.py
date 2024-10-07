h,m=map(int, input().split())
r=int(input())
if m+r<60:
    m=m+r
elif m+r==60:
    m=0
    h=h+1 
elif m+r>60:
    h=h+(m+r)//60
    m=(m+r)%60
if h>=24:
    h=h-24
print(h,m)