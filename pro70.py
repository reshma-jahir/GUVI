nk11=int(input())
tm=3
s=3
l=[]
l.append(3)
for i in range(1,nk11+1):
    if tm==1:
        tm=2*s
        s=tm
        l.append(tm)
    else:
        tm=tm-1
        l.append(tm)
print(l[nk11-1])
