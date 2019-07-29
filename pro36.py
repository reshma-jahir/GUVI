pin=input()
q=list(map(int,input().split()))
cas=0
for i in range(0,len(q)-2):
    for j in range(i+1,len(q)-1):
        for k in range(j+1,len(q)):
            if q[i]>q[j] and q[j]>q[k]:
                cas+=1
print(cas)
