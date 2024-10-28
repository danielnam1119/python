a=int(input())
blank=a-1
for i in range(1, a+1):
    star=i*2-1
    print(" "*blank+"*"*star)
    blank=blank-1
m=3
for i in range(1, a):
  print((" "*i)+"*"*(2*a-m))
  m+=2