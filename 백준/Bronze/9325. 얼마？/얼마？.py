car=int(input())
for i in range(car):
    total=0
    price=int(input())
    opt=int(input())
    for j in range(opt):
        a, b=map(int, input().split())
        total += a*b
    total += price
    print(total)