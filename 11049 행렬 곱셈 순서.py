# 행렬 곱셈 순서

import sys
input = sys.stdin.readline

n = int(input())
size_matrix = []
for _ in range(n):
    size_matrix.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1,n):    # n개를 곱했다면 i는 n-1
    for j in range(n-i):    # 몇번째 행렬
        if i==1:        # 2개를 곱했다면 
            dp[j][j+i] = size_matrix[j][0] * size_matrix[j][1] * size_matrix[j+1][1]
            continue
        dp[j][j+i] = 2**32 # 최대값
        for k in range(j,j+i):  
            dp[j][j+i] = min(dp[j][j+i],dp[j][k] + dp[k+1][j+i] + size_matrix[j][0]*size_matrix[k][1]*size_matrix[j+i][1])

print(dp[0][-1])