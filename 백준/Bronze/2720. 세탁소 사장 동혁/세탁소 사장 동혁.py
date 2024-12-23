t=int(input())
for i in range(t):
    a=int(input())
    q=a//25
    d=a%25//10
    n=a%25%10//5
    p=a%25%10%5//1
    print(q, d, n, p)