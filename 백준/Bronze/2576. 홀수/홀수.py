oddnum=[]
for i in range(7):
    inp=int(input())
    if inp%2!=0:
        oddnum.append(inp)
if len(oddnum)==0:
    print(-1)
else:
    print(sum(oddnum))
    print(min(oddnum))