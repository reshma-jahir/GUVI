pin=input()
b=input()
c=pin.index('|')
d=len(pin)+len(b)
if d%2==0:
    print("Impossible")
else:
    if c<=d//2-1:
        pin=b+pin
    else:
        pin=pin+b
    c=pin.index('|')
    if c!=d//2-1 and c!=d//2:
        print("Impossible")
    else:
        print(pin)
