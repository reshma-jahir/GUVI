chate=int(input())
valu=list(map(int,input().split()[:chate]))
valu.sort()
for i in valu:
  print(i,end=" ")
