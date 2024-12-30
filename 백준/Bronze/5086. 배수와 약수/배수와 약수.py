while True:
    a, b=map(int, input().split())
    if a==0 and b==0:
        break
    elif b%a==0 or a%b==0:
        if a<b:
            print("factor")
        elif a>b:
            print("multiple")
    elif b%a!=0 and a%b!=0:
        print("neither")