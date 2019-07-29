pin,q,r,s=map(int,input().split())
list1=list(map(int,input().split()))
list2=[]
for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        for k in range(j,len(list1)):
            list2.append(q*list1[i]+r*list1[j]+s*list1[k])
print(max(list2))
