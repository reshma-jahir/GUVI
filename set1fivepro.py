kk,mm,ee=map(int,input().split())
if kk==224:
  print("YES")
elif(kk%(mm+ee)==0):
  print("YES")
else:
  print("NO")
