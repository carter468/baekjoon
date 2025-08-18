# 충성! 파란댕댕이
# Platinum 4, exponentiation by squaring

import sys
input = sys.stdin.readline
MOD = 10**9+9

def pow(A,p):
    def mul(A,B):
        result = [[0]*L for _ in range(L)]
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    result[i][j] += A[i][k]*B[k][j]
                result[i][j] %= MOD
        return result
    
    if p == 1: return A

    B = pow(A,p//2)
    if p%2 == 0: return mul(B,B)
    else: return mul(mul(B,B),A)

N,M,T = map(int,input().split())

L = N*2
arr = [[0]*L for _ in range(L)]
for _ in range(M):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        a,b = q[1]-1,q[2]-1
        arr[a][b] += 1
        arr[b][a] += 1
    else:
        a,b,c = q[1]-1,q[2]-1,q[3]-1
        for x,y in (a,b),(b,a),(a,c),(c,a),(b,c),(c,b):
            arr[x][y+N] += 1
            arr[y+N][y] = 1
            
print(*pow(arr,T)[0][:N],sep='\n')