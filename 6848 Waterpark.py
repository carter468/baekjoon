# Waterpark
# Gold 5, DP

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
while True:
    x,y = map(int,input().split())
    if x == 0: break
    graph[y].append(x)

dp = [0]*(N+1)
dp[1] = 1
for i in range(2,N+1):
    for j in graph[i]:
        dp[i] += dp[j]
print(dp[N] if dp[N] > 0 else 0)