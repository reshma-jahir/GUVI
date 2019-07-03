chm=int(input())
fabt,fabot=0,1
print(fabot,end=" ")
for i in range(1,chm):
  faboot=fabt+fabot
  print(faboot,end=" ")
  fabt,fabot=fabot,faboot
