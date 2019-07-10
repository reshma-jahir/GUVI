sab,sar=map(str,input().split())
yast=0
if len(sab)>len(sar):
	sab,sar=sar,sab
p=0
while p<len(sab):
	  yas+=(ord(sar[p])-ord(sab[p]))
	  p+=1
for p in range(p,len(sar)):
	  yas+=ord(sar[p])-ord('a')+1
print(yast)
