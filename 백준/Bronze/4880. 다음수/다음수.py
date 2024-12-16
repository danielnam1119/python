while True:
    n=list(map(int, input().split()))
    if n[0]==0 and n[1]==0 and n[2]==0:
        break
    if n[1]-n[0]==n[2]-n[1]:
        print("AP", n[2]+n[2]-n[1])
    else:
        print("GP", n[2]*(n[2]//n[1]))