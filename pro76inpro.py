pp, Qp, Fp, Kd = map(int, input().split())
cnt = 0
Dvd = Qp-Fp
if (Dvd >= 0):
    S1 = (pp-Fp)*2
    for X in range (Kd):
        if (X == Kd-1):
             S1 =S1/ 2
        if (Dvd < S1):
            Dvd= Qp
            cnt += 1
        Dvd = Dvd - S1
        if (Dvd < 0):
            cnt = -1
            break
        S1 = 2*pp - S1
    print (cnt)
else:
    print (-1)
