# 문자열 제작
# Gold 1, combinatorics, FIT

MOD = 998244353

n,m = map(int,input().split())

fac = [0,1]
rfac = [1,1]
for i in range(2,200001):
    fac.append(fac[-1]*i%MOD)
    rfac.append(pow(fac[-1],MOD-2,MOD))

r = (fac[n]*rfac[m]*rfac[n-m]%MOD)*pow(25,n-m,MOD)%MOD
result = r
for i in range(m+1,n+1):
    result = (result+(fac[n]*rfac[i]*rfac[n-i]*pow(25,n-i,MOD)*2))%MOD
print(r*result%MOD)