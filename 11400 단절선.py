# 단절선
# Platinum 4, DFS, articulation

import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(x,parent):
    global order
    order += 1
    visited[x] = order
    m = order

    for nx in graph[x]:
        if nx == parent:
            continue
        if visited[nx]:
            m = min(m,visited[nx])
        else:
            r = dfs(nx,x)
            if r > visited[x]:
                bridges.append(sorted((x,nx)))
            m = min(m,r)
    
    return m

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = 0
visited = [0]*(V+1)
bridges = []

for i in range(1,V+1):
    if visited[i] == 0:
        dfs(i,0)

print(len(bridges))
for b in sorted(bridges):
    print(*b)