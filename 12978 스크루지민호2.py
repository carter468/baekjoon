# 스크루지 민호 2
# Gold 3, DP, tree DP

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(x,prev,c):
    if dp[x][c]: return dp[x][c]

    dp[x][c] = c
    for nx in graph[x]:
        if nx != prev:
            if c == 1:
                dp[x][c] += min(solve(nx,x,1),solve(nx,x,0))
            else:
                dp[x][c] += solve(nx,x,1)
    
    return dp[x][c]

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0]*2 for _ in range(n+1)]
print(min(solve(1,0,0),solve(1,0,1)))