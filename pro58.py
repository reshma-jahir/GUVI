pin = int(input())
q = []
d = pin//2 + pin
for i in range(1,pin+1):
  if i%2==0:
    q.append(i)
for i in range(1,pin+1):
  if i%2!=0:
    q.append(i)
for i in range(1,pin+1):
  if i%2==0:
    q.append(i)
print(d)
print(*q)
