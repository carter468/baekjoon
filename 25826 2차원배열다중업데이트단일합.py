# 2차원 배열 다중 업데이트 단일 합
# Gold 4, prefix sum

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(N)]

B = [[0]*(N+2) for _ in range(N+2)]
for _ in range(M-1):
    _,i1,j1,i2,j2,k = map(int,input().split())
    B[i1][j1] += k
    B[i2+1][j1] -= k
    B[i1][j2+1] -= k
    B[i2+1][j2+1] += k
for i in range(N):
    for j in range(N):
        B[i][j] += B[i][j-1]
for j in range(N):
    for i in range(N):
        B[i][j] += B[i-1][j]

_,i1,j1,i2,j2 = map(int,input().split())
result = 0
for i in range(i1,i2+1):
    for j in range(j1,j2+1):
        result += A[i][j]+B[i][j]
print(result)