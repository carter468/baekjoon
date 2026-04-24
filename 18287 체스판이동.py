# 체스판 이동
# Platinum 3, DP, exponentiation by squaring

def mul(A,B):
    result = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            t = 0
            for k in range(M):
                t += A[i][k]*B[k][j]
            result[i][j] = t%MOD
    return result

def pow(A,p):
    if p == 0: return E
    if p == 1: return A
    B = pow(A,p//2)
    if p%2 == 0: return mul(B,B)
    else: return mul(mul(B,B),A)

MOD = 10**9+7
N,M = map(int,input().split())

E = [[0]*M for _ in range(M)]
for i in range(M):
    E[i][i] = 1
odd = [[0]*M for _ in range(M)]
for i in range(M):
    if i-1 >= 0: odd[i][i-1] = 1
    if i+1 < M: odd[i][i+1] = 1
even = [[0]*M for _ in range(M)]
for i in range(M):
    even[i][i] = 1
    if i-1 >= 0: even[i][i-1] = 1
    if i+1 < M: even[i][i+1] = 1

x = pow(mul(odd,even),(N-1)//2)
if N%2 == 0: x = mul(x,odd)

print(sum([sum(x[i]) for i in range(M)])%MOD)