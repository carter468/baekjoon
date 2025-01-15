# 주민등록번호
# Gold 1, bruteforcing, DP, implementation

D = [[0,31,28,31,30,31,30,31,31,30,31,30,31],[0,31,29,31,30,31,30,31,31,30,31,30,31]]

S = input()

left,right,C = S[:8],S[8:18],S[-1]

if C == 'X':
    count = 0
    for y in range(1,10000):
        f = y%400 == 0 or (y%100 != 0 and y%4 == 0)
        y = str(y).zfill(4)
        for i in range(4):
            if left[i+4] not in ('X',y[i]): break
        else:
            for m in range(1,13):
                m = str(m).zfill(2)
                for i in range(2):
                    if left[i+2] not in ('X',m[i]): break
                else:
                    for d in range(1,D[f][int(m)]+1):
                        d = str(d).zfill(2)
                        for i in range(2):
                            if left[i] not in ('X',d[i]): break
                        else: count += 1
    count *= 10**(right.count('X'))
else:
    C = int(C)
    
    dp = [[0]*19 for _ in range(11)]
    dp[0][0] = 1
    w = [2]+list(range(10,1,-1))
    for i in range(1,11):
        if right[i-1] == 'X':
            arr = list(range(10))
        else:
            arr = [int(right[i-1])]
        for a in arr:
            for j in range(19):
                dp[i][(j+a*w[i-1])%19] += dp[i-1][j]

    count = 0
    w = list(range(10,2,-1))
    for y in range(1,10000):
        f = y%400 == 0 or (y%100 != 0 and y%4 == 0)
        y = str(y).zfill(4)
        k = 0
        for i in range(4):
            if left[i+4] not in ('X',y[i]): break
            k += int(y[i])*w[i+4]
        else:
            for m in range(1,13):
                kk = k
                m = str(m).zfill(2)
                for i in range(2):
                    if left[i+2] not in ('X',m[i]): break
                    kk += int(m[i])*w[i+2]
                else:
                    for d in range(1,D[f][int(m)]+1):
                        kkk = kk
                        d = str(d).zfill(2)
                        for i in range(2):
                            if left[i] not in ('X',d[i]): break
                            kkk += int(d[i])*w[i]
                        else:
                            kkk %= 19
                            if C != 0:
                                count += dp[-1][(C-kkk)%19]+dp[-1][(19-C-kkk)%19]
                            else:
                                count += dp[-1][(C-kkk)%19]

print(count)