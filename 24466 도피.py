# 도피
# Gold 4, DP, math

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

dp = [[0]*n for _ in range(10)]
dp[0][0] = 1
for i in range(9):
    for j in range(n):
        for a,b in graph[j]:
            dp[i+1][a] += dp[i][j]*b

result = [0,[]]
for i in range(n):
    if dp[9][i] > result[0]:
        result = [dp[9][i],[i]]
    elif dp[9][i] == result[0]:
        result[1].append(i)
k = 10**18
print(*result[1])
print(f'{result[0]//k}.{result[0]%k:018}')