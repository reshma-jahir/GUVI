v66=int(input())
k=list(map(int,input().split()))
s,f=0,[]
d=[x for x in range(1,v66+1)]
for i in k:
  if i in d:
    d.remove(i)
m=0
for i in range(0,v66-1):
  h=k[i]
  for j in range(i+1,v66):
    if h==k[j]:
      if h<d[m]:
        k[j]=d[m]
        s+=1
      else:
        k[i]=d[m]
        s+=1
      m+=1
print(s)
print(*k)
