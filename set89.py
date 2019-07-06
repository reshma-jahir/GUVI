aa1,bb2=map(int,input().split())
c3=aa1*bb2
for i in range(0,c3+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
