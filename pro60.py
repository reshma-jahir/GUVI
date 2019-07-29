pin = int(input())
a,val = 3,3
while pin > 0:
    if a == 0:
        val*=2
        a = val
    if pin==1:
        print(a)
        break
    pin -= 1
    a -= 1
