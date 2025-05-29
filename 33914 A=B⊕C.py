# A = B ⊕ C
# Gold 5, math, combinatorics, modular multiplicative inverse 

MOD = 10**9+7

X,Y = map(int,input().split())

if X%2 == 1: exit(print(0))
a = X//2
if (Y-a)%3 != 0 or Y < a: exit(print(0))
b = (Y-a)//3

n,k = a+b,b
fac = [1]
for i in range(n):
    fac.append(fac[-1]*(i+1)%MOD)
inv = [1]*(n+1)
inv[-1] = pow(fac[-1],-1,MOD)
for i in range(n-1,-1,-1):
    inv[i] = inv[i+1]*(i+1)%MOD

print(pow(3,a,MOD)*fac[n]*inv[n-k]*inv[k]%MOD)