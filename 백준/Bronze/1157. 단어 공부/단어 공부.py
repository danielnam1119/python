s=input()
s=s.upper()
alp=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cnt=[]
for i in range(len(alp)):
    cnt.append(s.count(alp[i]))
m=max(cnt)
if cnt.count(m) >=2:
    print("?")
else:
    print(alp[cnt.index(m)])