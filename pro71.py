dk1=str(input())
vhh=str(input())
S=""
T1=0
T2=0
T=""
R=""
for X in range(0,len(dk1)):
    T1=ord(dk1[X])-96
    T2=ord(vhh[X])+T1
    if(T2>122):
        T2=T2-122
        T2=T2+96
    T=T+chr(T2)
print(T)
