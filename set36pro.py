def subseq(a): 
    num = len(a) 
    subseq = [1]*num 
    for i in range (1 , num): 
        for j in range(0 , i): 
            if a[i] > a[j] and subseq[i]< subseq[j] + 1 : 
                subseq[i] = subseq[j]+1
    maximum = 0
    for i in range(num): 
        maximum = max(maximum , subseq[i])  
    return maximum




ar=int(input()) 
a = list(map(int,input().split()))
print (subseq(a))
