cc=list(input())
pp=[]
for i in cc:
    if i not in pp:
        pp.append(i)
if(cc==pp):
    print("Yes")
else:
    print("No")
