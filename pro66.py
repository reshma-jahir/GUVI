pin, q, f, k = map(int, input().split())
cnt = 0
d = q-f
if (d >= 0):
    s = (pin-f)*2
    for i in range (k):
        if (i == k-1):
             s =s/ 2
        if (d < s):
            d= q
            cnt += 1
        d = d - s
        if (d < 0):
            cnt = -1
            break
        s = 2*pin - s
    print (cnt)
else:
    print (-1)
