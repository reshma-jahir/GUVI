cin=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
d=l1[::-1]
rest=''
for i in range(len(d)):
    rest=rest+str(d[i])+''
print(rest)
