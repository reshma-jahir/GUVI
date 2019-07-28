number=int(input())
lis=list(map(int,input().split()))
for j in lis:
    if lis.count(j)>1:
        print(j)
        break
else:
    print("unique")
