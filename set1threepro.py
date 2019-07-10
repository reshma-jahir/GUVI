rr,ss=input().split()
tt1=abs(len(rr)-len(ss))
for i in range(len(rr)):
  if len(ss)==1 and ss[i] in rr:
    break
  if rr[i]!=ss[i]:
    tt1=tt1+1
print(tt1)
