Pj1,Qj1=map(int,input().split())
Li=list(map(int,input().split()))[:Pj1]
rd=int(input())
S=(sum(Li)-Li[Qj1])//2
if (S==rd):
    print("Bon Appetit")
else:
    print(abs(S-rd))
