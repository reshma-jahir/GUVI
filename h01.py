num=int(input())
l=list(map(int,input().split()))
d=[]
for j in l:
    if l.count(j)>1:
        d.append(j)
c=set(d)
if len(c)==0:
    print("unique")
else:
    print(*c)
