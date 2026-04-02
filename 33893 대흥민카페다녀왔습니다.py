# 대흥민 카페 다녀왔습니다
# Platinum 4, floyd-warshall, DP

import sys
sys.setrecursionlimit(10**7)
INF = sys.maxsize

def f(x,s):
    state = (x,s)
    if state in visited:
        if visited[state] == -2:
            return INF
        return visited[state]

    m = 0
    visited[state] = -2

    for nx in graph[x]:
        if s>>nx&1: continue
        ns = 0
        for i in range(N):
            if s>>i&1:
                j = move[i][nx]
                if j == nx: break
                ns |= 1<<j
        else:
            t = f(nx,ns)
            if t == INF:
                visited[state] = t
                return t
            m = max(m,t+1)

    visited[state] = m
    return m

N,M,K = map(int,input().split())
graph = [[] for _ in range(N)]
dist = [[INF]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    graph[a].append(b)
    graph[b].append(a)
    dist[a][b] = 1
    dist[b][a] = 1
    
for i in range(N):
    dist[i][i] = 0
    graph[i].append(i)
    graph[i].sort()
    
s = sum(1<<(p-1) for p in map(int,input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

move = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in graph[i]:
            if dist[i][j] == dist[k][j]+1:
                move[i][j] = k
                break

visited = {}
m = f(0,s)
print(m+1 if m < INF else 'DaeHeungMin')