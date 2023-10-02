# 나무 위의 빗물
# Gold 5, dfs

import sys
input = sys.stdin.readline

n,w = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [0]*(n+1)
visit[1] = 1
q = [1]
count = 0
while q:
    x = q.pop()
    leaf = 1
    for nx in graph[x]:
        if not visit[nx]:
            visit[nx] = 1
            q.append(nx)
            leaf = 0
    if leaf: count += 1
    
print(w/count)