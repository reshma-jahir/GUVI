ec,li=map(int,input().split())
for i in range(ec+1,li):
    finally=i
    find=0
    while(i>0):
        dad=i%10
        find=find+(dad**3)
        i=i//10
        if(find==finally):
            print(find, end=" ")
