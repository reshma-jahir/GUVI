pin,q=map(int,input().split())
l = list(map(int,input().split()))
count = 0
for i in range(0,len(l)):
    if (l[i]+q)<=5:
        count+=1
print(count//3)
