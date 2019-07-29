pin=input()
l=list(set(pin))
q=1
a=0
check=False
while True:
    ch=l[a]
    for j in range(0,len(pin)-q):
        if ch in pin[j:j+q]:
            check=True
        else:
            check=False
            a+=1
            if a>=len(l):
             a=0
             q+=1
            break

    if check==True:
        break
print(q)
