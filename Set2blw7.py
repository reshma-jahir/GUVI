action=int(input())
ti=0
fot=action
while(fot>0):
    ft=fot%10
    ti=ti+(ft**3)
    fot=fot/10
if(action==ti):
    print("yes")
else:
    print("no")
