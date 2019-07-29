pin,q=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    k=86400-i
    q-=k
    c+=1
    if q<=0:
        break  
print(c)

