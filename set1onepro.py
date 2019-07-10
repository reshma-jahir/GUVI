def lus(str11,str12):
        if(str11 in str12):
            return str11
        else:
            return lus(str11[0:len(str11)-1],str12)
mem = int(input())
x= []
for _ in range(0,mem):
    x.append(input())
x.sort()
print(lus(x[0],x[mem-1]))
