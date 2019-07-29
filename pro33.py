pin=input()
for i in range(len(pin)):
  if(pin[i] < pin[i+1]):
    print(pin[i+1:])
    break
