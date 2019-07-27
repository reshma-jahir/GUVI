num=int(input())
pin=list(map(int,input().split()))
qin=sorted(pin)
for i in range(0,len(pin)):
    if(qin[i]!=pin[i]):
        print(i)
        break
