num,kit=input().strip().split(" ")
kit=int(kit)
i=0;
while i<len(num)-1 and kit:
	if(num[i]>num[i+1]):
		kit-=1
		num=num[:i]+num[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
rey=num[:len(num)-kit]
print(rey)
