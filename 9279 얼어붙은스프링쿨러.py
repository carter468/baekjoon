# 얼어붙은 스프링쿨러
# Gold 3, DP

import sys
sys.setrecursionlimit(9999)
input = sys.stdin.readline

def dfs(x):
    t = 0
    for nx,w in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            t += min(w,dfs(nx))
    return t if t > 0 else 10**9

while True:
    try:
        N,C = map(int,input().split())
    except:
        break

    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    visited = [False]*(N+1)
    visited[C] = True
    print(dfs(C))