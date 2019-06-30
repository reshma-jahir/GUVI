ex,oil=map(int,input().split())
for i in range(ex+1,oil):
    finally=i
    fine=0
    while(i>0):
        dad=i%10
        fine=fine+(dad**3)
        i=i//10
        if(fine==finally):
            print(fine, end=" ")
