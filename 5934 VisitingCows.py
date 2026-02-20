# Visiting Cows
# Gold 2, DP

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(x,c,p):
    if dp[x][c] != -1: return dp[x][c]

    dp[x][c] = c
    for nx in graph[x]:
        if nx == p: continue
        if c == 0:
            dp[x][c] += max(solve(nx,1,x),solve(nx,0,x))
        else:
            dp[x][c] += solve(nx,0,x)
    return dp[x][c]

N = int(input())
graph = [[] for _ in range(N+1)]
graph[0] = [1]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[-1]*2 for _ in range(N+1)]
print(solve(0,0,0))