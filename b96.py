A66,B66,C66=map(int,input().split())
num=0
for i in range(0,C66):
    num=num+A66
    A66=A66+B66
print(num)
