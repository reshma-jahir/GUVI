import sys
def palindrome(dk1):
    if len(dk1) == 1:
        return False
    if dk1 == dk1[::-1]:
        return True
    return False
dk1 = input()
num = len(dk1)
for i in range(num-1, 0, -1):
    for j in range(0, num-i):
        i1 = j
        i2 = j+i+1
        d2 = dk1[i1:i2]
        if palindrome(d2):
            print(num-len(d2))
            sys.exit()
