pp,mm=map(int,input().split())
nnn=[]
tt=[]
gcd=1
for i in range(1,pp+1):
    if(pp%i==0):
        nn.append(i)
for j in range(1,mm+1):
    if(mm%j==0):
        tt.append(j)
for y in nnn:
    if y in tt:
        gcd=gcd*y
print(gcd)
