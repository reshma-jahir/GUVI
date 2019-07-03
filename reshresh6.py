chx=input()
fit=0
for i in range(len(chx)):
  if(chx[i].isdigit() or chx[i].isalpha() or chx[i]==(" ")):
    continue
  else:
    fit+=1
print(fit)
