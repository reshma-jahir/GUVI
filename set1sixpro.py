u44=int(input())
o44=list(map(int,input().split()))
c=0
for i in range(0,u44-2):
	for j in range(1,u44-1):
		for k in range(2,u44):
			if(o44[i]<o44[j] and o44[j]<o44[k]):
				c+=1
print(c)
