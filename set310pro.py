n11=input()
ca=0
for i in range(0,len(n11)):
    ss=n11[0:i]+n11[i+1::]
    if int(ss)%8==0:
        ca=1
        break
if ca==1:
    print("yes")
else:
  print("no")
