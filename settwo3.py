var=int(input())
for i in range(2,var):
  if(var%i==0):
    print("no")
    break
else:
  print("yes")
