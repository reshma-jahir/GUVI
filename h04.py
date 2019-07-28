num=int(input())
listval=list(map(int,input().split()))
for i in listval:
    if listval.count(i)==1:
        print(i)
        break
