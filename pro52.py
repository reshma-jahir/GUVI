pin=input().split()
q=input().split()
r=input().split()
s=input().split()
if(pin[0]==q[0] or pin[0]==r[0] or pin[0]==s[0]) and (pin[1]==q[1] or pin[1]==r[1] or pin[1]==s[1]):
    print("yes")
else:
    print("no")
