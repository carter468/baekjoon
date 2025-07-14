# 보석 줍기
# Platinum 5, DFS, bitmask

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
gem = [int(input()) for _ in range(K)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

count = 0
visited = [[False]*(1<<K) for _ in range(N+1)]
visited[1][0] = True
q = [(1,0,0)]
while q:
    x,s,c = q.pop()
    if x == 1:
        if x in gem and not s>>gem.index(x)&1: count = max(count,c+1)
        else: count = max(count,c)
    
    if x in gem:
        idx = gem.index(x)
        if not s>>idx&1:
            ns = s|1<<idx
            nc = c+1
            for nx,d in graph[x]:
                if not visited[nx][ns] and d >= nc:
                    visited[nx][ns] = True
                    q.append((nx,ns,nc))

    for nx,d in graph[x]:
        if not visited[nx][s] and d >= c:
            visited[nx][s] = True
            q.append((nx,s,c))

print(count)