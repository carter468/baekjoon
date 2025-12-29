# 은하 충돌
# Gold 2, DP, DAG

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(u):
    if dp[u] != -1: return dp[u]

    dp[u] = S[-u-1] if u < 0 else 0
    m = 0
    for v in graph[u]:
        m = max(m,solve(v))
    dp[u] += m
    return dp[u]

N,M,E = map(int,input().split())
graph = [[] for _ in range(N+M+1)]
dist = [10**10]*(N+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append(v)
    if u > 0: dist[u] = min(dist[u],w)
    if v > 0: dist[v] = min(dist[v],w)
S = tuple(map(int,input().split()))
G = int(input())

dp = [-1]*(N+M+1)
print(['HAPPY','SAD'][solve(1) < dist[G]])