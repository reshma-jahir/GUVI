lawt=input()
yawt=map(int,input().split())
pawt=[]
for g in yawt:
    enum=bin(g)
    pawt.append(enum)
fraud=sorted(pawt)
fraud.reverse()
for h in fraud:
    print(int(h,2))
