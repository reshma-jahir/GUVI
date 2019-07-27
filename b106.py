pin,qin=map(int,input().split())
count=0
r=list(map(int,input().split()))
for i in r:
    if(i%2!=0):
        count=count+1
    if(count==qin):
        print(i)
        break
