gef11,sef11=map(int,input().split())
maxima=max(gef11,sef11)
while(1):
 if(maxima%gef11==0 and maxima%sef11==0):
  print(maxima)
  break
 maxima+=1
