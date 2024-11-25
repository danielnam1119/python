subject=int(input())
grade=list(map(int, input().split()))
m=max(grade)
for i in range(subject):
    grade[i]=grade[i]/m*100
print(sum(grade)/subject)