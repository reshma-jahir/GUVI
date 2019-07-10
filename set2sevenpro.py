bhavt,sent = input().split()
sent = int(sent)
fake = False
bent = list(map(int,input().split()))
for i in range(len(bent)):
    for j in range(len(bent)):
        if bent[i]+bent[j] == sent:
            fake = True
print("yes" if fake else "no") 
