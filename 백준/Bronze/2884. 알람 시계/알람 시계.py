h,m=map(int, input().split())
if h>0:
    if m<45:
        print(h-1,m+15)
    elif m>=45:
        print(h,m-45)
else:
    if m<45:
        print(h+23,m+15)
    elif m>=45:
        print(h,m-45)