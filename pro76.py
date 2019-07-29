pp, Qp, Fp, Kd = map(int, input().split())
cnt = 0
Dv = Qp-Fp
if (Dv >= 0):
    S1 = (pp-Fp)*2
    for X in range (Kd):
        if (X == Kd-1):
             S1 =S1/ 2
        if (Dv < S1):
            Dv= Qp
            cnt += 1
        Dv = Dv - S1
        if (Dv < 0):
            cnt = -1
            break
        S1 = 2*pp - S1
    print (cnt)
else:
    print (-1)
