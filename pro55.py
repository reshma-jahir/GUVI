pin,q = map(int,input().split())
a = list(map(int,input().split()))
b,cin = 0,[]
for i in range(0,len(a)):
  t = i
  for p in range(0,len(a)):
    for l in range(0,q):
      if l == q-1:
        try:
          b += a[pin+i]
        except IndexError:
            t = t-1
            b +=a[t]
      else:
        b += a[i]
    cin.append(b)
    b = 0
for i in range(0,len(a),q):
  b = sum(a[i:i+q])
  cin.append(b)
print(*sorted(set(cin)))
