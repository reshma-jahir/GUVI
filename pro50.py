pin,q=map(int,input().split())
pinq=[]
for i in range(q):
  pinq.append(list(map(int,input().split())))
w=10000000
f=0
for i in range(q):
  if pinq[i][0]==1:
    s=pinq[i][1]
    c=pinq[i][2]
    for j in range(i+1,q):
      if pinq[j][0]==s:
        s=pinq[j][1]
        c+=pinq[j][2]
    if c<w and s==pin:
      w=c
      f+=1
if f==0:
  print(-1)
else:
  print(w)
