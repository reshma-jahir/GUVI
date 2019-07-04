Names=int(input())
sar=0
i=0
while(Names>0):
    i=Names%10
    sar=sar+i
    Names=Names//10
print(sar)
