width=[]
height=[]
for i in range(3):
    w, h=map(int, input().split())
    width.append(w)
    height.append(h)
if width[0]==width[1]:
    a=width[2]
elif width[0]==width[2]:
    a=width[1]
elif width[1]==width[2]:
    a=width[0]
if height[0]==height[1]:
    b=height[2]
elif height[0]==height[2]:
    b=height[1]
elif height[1]==height[2]:
    b=height[0]
print(a,b)