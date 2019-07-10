chatr=int(input())
ger=[]
dog=0
for h in range (0,chatr+1):
    dog=abs((2**h)-chatr)
    ger.append(dog)
kall=min(ger)
print(kall)
