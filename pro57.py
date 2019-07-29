pin,q=map(str,input().split())
count=0
for i in range(0,len(pin)):
    for j in range(0,len(q)):
        if pin[i]==q[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
