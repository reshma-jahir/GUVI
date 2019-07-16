num=int(input())
l=[]
m=len(str(num))
s=0
for _ in range(m):
	s+=9
for i in range(num-s,num):
	r=0
	d=i
	while(d>0):
		r+=(d%10)
		d=d//10
	if(r+i==num):
		l.append(i)
print(len(l),*l,sep='\n')
