vv1=int(input())
vv2=list(map(int,input().split()))
ans=int(vv1/2)
r1=vv2[:ans]
r2=vv2[ans::]
if ((sum(r1)//len(r1))==(sum(r2)//len(r2))):
    print("yes")
else:
    print("no")
