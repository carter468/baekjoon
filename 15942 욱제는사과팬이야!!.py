# 욱제는 사과팬이야!!
# Gold 5, DP

# import sys
# M = 10**9+9

# n,m = map(int,input().split())
# arr = [sys.stdin.readline() for _ in range(n)]

# dp = [[0]*m for _ in range(n)]
# dp[-1][-1] = 1
# for i in range(n-1,-1,-1):
#     for j in range(m-1,-1,-1):
#         x,y = i-1,j
#         if 0 <= x < n and arr[x][y] in 'BS':
#             dp[x][y] = (dp[x][y]+dp[i][j])%M
#         x,y = i,j-1
#         if 0 <= y < m and arr[x][y] in 'BE':
#             dp[x][y] = (dp[x][y]+dp[i][j])%M

# result = 0
# for d in dp:
#     result = (result+sum(d))%M
# print(result)

import sys
M = 10**9+9

n,m = map(int,input().split())
arr = [sys.stdin.readline() for _ in range(n)]

dp = [[0]*m for _ in range(n)]
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if arr[i][j] == 'X': dp[i][j] = 1
        elif arr[i][j] == 'E': dp[i][j] = dp[i][j+1]
        elif arr[i][j] == 'S': dp[i][j] = dp[i+1][j]
        else: dp[i][j] = (dp[i+1][j]+dp[i][j+1])%M

result = 0
for d in dp:
    result = (result+sum(d))%M
print(result)