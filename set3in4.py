check=int(input())
valid=list(map(int,input().split()[:check]))
valid.sort()
for i in valid:
  print(i,end=" ")
