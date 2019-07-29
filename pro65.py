pin,q=map(int,input().split())
li=list(map(int,input().split()))[:pin]
r=int(input())
s=(sum(li)-li[q])//2
if (s==r):
    print("Bon Appetit")
else:
    print(abs(s-r))
