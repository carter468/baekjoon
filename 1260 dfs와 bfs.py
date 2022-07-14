# dfs와 bfs

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# n,m,v = 4,5,1
# edge = [[1,2],[1,3],[1,4],[2,4],[3,4]]

# graph = [[] for _ in range(n+1)]
# for x in edge:
#     graph[x[0]].append(x[1])
#     graph[x[1]].append(x[0])

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]    # graph[i] : i와 연결된 노드번호
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)    
    graph[b].append(a)

def dfs(v):
    visited[v] = 1
    print(v,end=' ')
    graph[v].sort()
    for x in graph[v]:
        if visited[x] == 0:
            dfs(x)

def bfs(v):
    for i in range(1,n+1):
        if i != v:
            visited[i] = 0
    visited[v] = 1
    print(v,end=' ')
    q.append(v)
    while q:
        u = q.pop(0)
        graph[u].sort()
        for x in graph[u]:
            if visited[x] == 0:
                visited[x] = 1
                print(x,end=' ')
                q.append(x)

visited = [0] * (n+1)
dfs(v)
print()

visited = [0] * (n+1)
q = []
bfs(v)

