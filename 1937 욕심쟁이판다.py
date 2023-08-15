# 욕심쟁이 판다
# Gold 3, DP, DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i,j):
    if dp[i][j] == -1:
        dp[i][j] = 0
        for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0 <= x < n and 0 <= y < n and arr[x][y] > arr[i][j]:
                dp[i][j] = max(dp[i][j],dfs(x,y))
    return dp[i][j]+1

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[-1]*n for _ in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))
print(result)