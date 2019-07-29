pin=int(input())
while pin%10==0:
  pin=pin//10
pin=str(pin)
re=pin[::-1]
if pin==re:
  print("yes")
else:
    print("no")
