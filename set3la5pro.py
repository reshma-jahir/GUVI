number=input()
level=list(map(int,input().split()))
maximum=0
i=0
while(i<len(level)-1):
    count=0
    while(i<len(level)-1 and level[i]<level[i+1]):
        count+=1
        i+=1
    if(count>maximum):
        maximum=c
    i+=1
print(maximum+1)
