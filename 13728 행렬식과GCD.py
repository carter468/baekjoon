# 행렬식과 GCD
# Platinum 4, linear algebra, number theory

MOD = 10**9+7

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

N = int(input())

f = [1]*(N+2)
for i in range(3,N+2):
    f[i] = (f[i-1]+f[i-2])%MOD
result = 0
for i in range(1,N+1):
    result += f[gcd(i+1,N+1)]
print(result%MOD)