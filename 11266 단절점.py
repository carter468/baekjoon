# 단절점
# Platinum 4, DFS, articulation

import sys
sys.setrecursionlimit(11111)
input = sys.stdin.readline

def dfs(x,f):
    global order
    order += 1
    visited[x] = order

    c = 0
    m = order
    for nx in graph[x]:
        if visited[nx] != 0:
            m = min(m,visited[nx])
            continue
        
        c += 1
        r = dfs(nx,False)
        if not f and r >= visited[x]: result.add(x)

        m = min(m,r)
    if f and c >= 2: result.add(x)
    
    return m

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

order = 0
visited = [0]*(V+1)
result = set()
for i in range(1,V+1):
    if visited[i] == 0:
        dfs(i,True)

print(len(result))
if result: print(*sorted(result))