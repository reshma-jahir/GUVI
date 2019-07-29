pin,q=map(int,input().split())
li=list(map(int,input().split()))
if q==1:
  print(min(li))
elif q==2:
  print(max(li[0],li[pin-1]))
else:
  print(max(li))
