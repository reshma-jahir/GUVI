    
ber=int(input())
for i in range(2,n):
    if ber%i==0:
        print("no")
        break
else:
    print("yes")
