import math
chat,chot=map(int,input().split())
ohot=[]
gaat=list(map(int,input().split()))
for p in range(0,cho):
    lovet,hutt=map(int,input().split())
    ohot.append([lovet,hutt])
for p in ohot:
    kaat=p[0]-1
    laat=p[1]-1
    print(math.gcd(gaat[kaat],gaat[laat]))
