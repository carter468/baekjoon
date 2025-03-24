# 선우의 셋리스트
# Platinum 5, DP, exponentiation by squaring

import sys
input = sys.stdin.readline

def matpow(mat,p):
    def matmul(a,b):
        mul = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                x = 0
                for k in range(5):
                    x += a[i][k]*b[k][j]
                mul[i][j] = x%MOD
        return mul
    
    if p == 1: return mat
    m = matpow(matmul(mat,mat),p//2)
    if p%2 == 0: return m
    else: return matmul(m,mat)

MOD = 10**9+7

N,M = map(int,input().split())

arr = [[0]*5 for _ in range(5)]
for i in range(4):
    arr[i+1][i] = 1
for _ in range(M):
    arr[0][int(input())-1] += 1

dp = [1]+[0]*5
for i in range(1,6):
    for j in range(1,i+1):
        dp[i] += dp[i-j]*arr[0][j-1]

if N <= 5:
    print(dp[N])
else:
    result = matpow(arr,N-5)
    answer = 0
    for i in range(5):
        answer += result[0][i]*dp[5-i]
    print(answer%MOD)