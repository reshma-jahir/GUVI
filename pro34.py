pin,qin=map(int,input().split())
n=0
Lst=[]
for i in range(pin):
      Lst.append(input())
for j in range(pin):
      for pin in range(qin-1):
            if(Lst[j][pin]!='R' and Lst[j][pin+1]!='R'):
                  n=n+3
            elif(Lst[j][pin]!='G' and Lst[j][pin+1]!='G'):
                  n=n+5
print(n)
