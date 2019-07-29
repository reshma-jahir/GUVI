pin=int(input())
q=[int(i) for i in input().split()]
d=0
for i in range(1,pin-1):
    if q[i]<q[i-1] and q[i]<q[i+1]:
        d+=1
    elif q[i]>q[i-1] and q[i]>q[i+1]:
        d+=1
print(d) 
