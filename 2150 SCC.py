# Strongly Connected Component

# Tarjan 알고리즘

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# v,e = map(int,input().split())
# graph = [[] for _ in range(v+1)]
# for _ in range(e):
#     a,b = map(int,input().split())
#     graph[a].append(b)

# stack = []
# low = [-1]*(v+1)
# ids = [-1]*(v+1)
# visited = [0] *(v+1)
# idid = 0
# result = []

# def dfs(x,low,ids,visited,stack):
#     global idid
#     ids[x] = idid
#     low[x] = idid
#     idid += 1
#     visited[x] = 1
#     stack.append(x)

#     for nx in graph[x]:
#         if ids[nx] == -1:
#             dfs(nx,low,ids,visited,stack)
#             low[x] = min(low[x],low[nx])
#         elif visited[nx] == 1:
#             low[x] = min(low[x],ids[nx])

#     w = -1
#     scc = []
#     if low[x] == ids[x]:
#         while w != x:
#             w = stack.pop()
#             scc.append(w)
#             visited[w] = -1
#         result.append(sorted(scc))

# for i in range(1,v+1):
#     if ids[i] == -1:
#         dfs(i,low,ids,visited,stack)
# print(len(result))
# for x in sorted(result):
#     print(*x,-1)

# kosaraju 알고리즘

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
graph_r = [[] for _ in range(v+1)]
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph_r[b].append(a)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
    stack.append(x)

def dfs_r(x):
    visited[x] = 1
    scc.append(x)
    for i in graph_r[x]:
        if visited[i] == 0:
            dfs_r(i)

stack = []
visited = [0] * (v+1)
for i in range(1,v+1):
    if visited[i] == 0:
        dfs(i)

visited = [0] * (v+1)
ans = []
while stack:
    scc = []
    x = stack.pop()
    if visited[x] == 0:
        dfs_r(x)
        ans.append(sorted(scc))
print(len(ans))
for x in sorted(ans):
    print(*x,-1)