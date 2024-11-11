while True:
    a=input().split()
    count=0
    if a[0]=="#":
        break
    else:
        for i in range(1, len(a)):
            a[i]=a[i].lower()
            for j in a[i]:
                if j==a[0]:
                    count=count+1
    print(a[0], count)