chat,chet=map(int,input().split())
kaat=[]
shut=[]
shat=[int(p) for p in input().split() ]
for g in range(0,chet):
    usat,unt=map(int,input().split())
    for h in range(usat-1 ,unt):
        shut.append(shat[h])
    xaat=sorted(shut)
    kaat.append(min(shut))
    del shut[:]
for o in range(0,len(kaat)):
    print(kaat[o])
