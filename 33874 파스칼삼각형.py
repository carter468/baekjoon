# 파스칼 삼각형
# Platinum 4, combinatorics, FLT, modular multiplicative inverse

MOD = 10**9+7

N = int(input())

if N == 2: print(0,3)
elif N == 3: print(1,4)
elif N == 4: print(2,4)
elif N == 5: print(3,6)
else:
    n = N-2
    k = n//2
    fac = [1]
    for i in range(n):
        fac.append(fac[-1]*(i+1)%MOD)
    inv = [1]*(n+1)
    inv[-1] = pow(fac[-1],-1,MOD)
    for i in range(n-1,-1,-1):
        inv[i] = inv[i+1]*(i+1)%MOD
    
    if N%2 == 0: c = 2
    else: c = 4
    print(fac[n]*inv[n-k]*inv[k]%MOD,c)