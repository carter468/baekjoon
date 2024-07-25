# Who is taller?
# Gold 5, DFS

import sys
input = sys.stdin.readline

def dfs(s,e):
    queue = [s]
    visited = [False]*(n+1)
    visited[s] = True
    while queue:
        x = queue.pop()
        if x == e: return True
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
    return False

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
p,q = map(int,input().split())

if dfs(p,q): print('yes')
elif dfs(q,p): print('no')
else: print('unknown')