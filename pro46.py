pin=int(input())
q=list(map(int,input().split()))
a=0
b=0
q.sort(reverse=True)
for i in q:
  q=a+i
  if b>q:
    a=q
  else:
    a=b
    b=q
print(a,b)
