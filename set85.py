strgs=list(input())
if len(strgs)%2==0:
    strgs[int(len(strgs)/2)] ='*'
    strgs[int(len(strgs)/2)-1]='*'
else:
    strgs[int(len(strgs)/2)] ='*'
for i in range(0,len(strgs)):
    print(strgs[i],end='')
