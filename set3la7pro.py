Aa,Bb=map(int,input().split())
Cc=list(map(int,input().split()))
pr=list(map(int,input().split()))
qr=[]
ar=0
for i in range(Aa):
    x=pr[i]/Cc[i]
    qr.append(x)
while Bb>=0 and len(qr)>0:
    mindex=qr.index(max(qr))
    if Bb>=Cc[mindex]:
        ar=ar+pr[mindex]
        Bb=Bb-Cc[mindex]
    Cc.pop(mindex)
    pr.pop(mindex)
    qr.pop(mindex)
print(ar)
