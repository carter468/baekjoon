# 리그 오브 레전설 (Large)
# Gold 1, exponentiation by squaring

MOD = 10**9+7

def mul(A,B):
    result = [[0]*(M+1) for _ in range(M+1)]
    for i in range(M+1):
        for j in range(M+1):
            for k in range(M+1):
                result[i][j] += A[i][k]*B[k][j]
            result[i][j] %= MOD
    return result

def pow(A,p):
    if p == 1: return A

    B = pow(A,p//2)
    if p%2 == 0: return mul(B,B)
    else: return mul(mul(B,B),A)

N,M = map(int,input().split())

arr = [[0]*(M+1) for _ in range(M+1)]
for i in range(M):
    arr[i][i+1] = 1
arr[-1][-1],arr[-1][-M] = 1,1

if N == M: print(2)
elif N < M: print(1)
else:
    result = pow(arr,N-M)
    print((sum(result[-1][:-1])+result[-1][-1]*2)%MOD)