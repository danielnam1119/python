angle={}
for i in range(3):
    a=int(input())
    angle[i+1]=a
if angle[1]+angle[2]+angle[3]!=180:
    print("Error")
elif angle[1]==angle[2] and angle[2]==angle[3]:
    print("Equilateral")
elif angle[1]==angle[2] or angle[2]==angle[3] or angle[1]==angle[3]:
    print("Isosceles")
else:
    print("Scalene")