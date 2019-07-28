num=int(input())
d=[int(x) for x in input().split()]
x=[]
for j in range(0,len(d)):
    if j==d[j]:
        x.append(j)
if len(x)==0:
    print(-1)
        
print(*x)
