aa=input().split()
total=int(aa[0])
coin=int(aa[1])
l=input().split()
l=[int(i) for i in l]
l=sorted(l,reverse=True)
tem=0
count=0
for i in range(0,len(l)):
  while True:
    if(tem==coin):
      break
    elif(tem>coin):
      count-=1
      tem-=l[i]
      break
    elif(tem<coin):
      tem+=l[i]
      count+=1
print(count)
