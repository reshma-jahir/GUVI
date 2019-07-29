pit,qrt=map(str,input().split())
ct=0
for i in range(0,len(pit)):
    for j in range(0,len(qrt)):
        if pit[i]==qrt[j]:
            ct+=1
if ct>=2:
    print("yes")
else:
    print("no")
