Dk11=input()
Qt=[]
for X in Dk11:
  if X not in Qt:
    Qt.append(X)
  else:
    break  
print(len(Qt))
