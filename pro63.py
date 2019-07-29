pin=input()
q=[]
for i in pin:
  if i not in q:
    q.append(i)
  else:
    break  
print(len(q))
