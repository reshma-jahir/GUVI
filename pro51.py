pin=int(input())
l=list(map(int,input().split()))
q=[]
r=1
for i in range(pin):
  v=l[i:]
  ans=len(v)
  for j in range(ans-1):
    if v[j]>0 and v[j+1]<0:
      r=r+1
    elif v[j]<0 and v[j+1]>0:
      r=r+1
    else:
      break
  q.append(str(r))
  r=1
print(" ".join(q))
