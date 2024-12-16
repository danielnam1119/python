while True:
    n=input()
    if n=="0":
        break
    while len(n)>1:
        n=sum(list(map(int,list(n))))
        n=str(n)
    print(n)