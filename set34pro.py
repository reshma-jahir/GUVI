number = int(input())
rest = []
for i in range(pow(2, number)):
    rest.append(bin(i)[2:].zfill(number))
rest.sort(key=(lambda x: x.count('1')))
for i in rest:
    print(i) 
