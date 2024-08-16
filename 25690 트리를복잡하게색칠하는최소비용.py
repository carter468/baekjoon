# 트리를 복잡하게 색칠하는 최소 비용
# Gold 3, DP

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(x,y):
    if dp[x][y] != sys.maxsize: return dp[x][y]
    
    dp[x][y] = cost[x][y]
    for nx in graph[x]:
        if y == 0: dp[x][y] += min(solve(nx,0),solve(nx,1))
        else: dp[x][y] += solve(nx,0)
    return dp[x][y]

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    p,c = map(int,input().split())
    graph[p].append(c)
cost = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[sys.maxsize]*2 for _ in range(n)]
print(min(solve(0,0),solve(0,1)))
