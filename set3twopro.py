aa=int(input())
bb=list(map(int,input().split()))
su=0
se=0
for i in range(aa):
	if i%2==0:
		su=su+bb[i]
	else:
		se+=bb[i]
print(max(su,se))
