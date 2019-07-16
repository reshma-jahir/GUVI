num=int(input())
l=list(map(int,input().split()))
l=sorted(l)
sum=0
cc=0
for i in l:
	if(sum<=i):
		cc+=1
	sum+=i
print(cc)
