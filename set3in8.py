post=int(input())
guy=list(map(int,input().split()[:post]))
for p in range(post):
  print(guy[p],p)
