# 트리 부수기
# Gold 3, DFS

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

depth = [-1]*N
depth[0] = 0
q = [0]
while q:
    x = q.pop()
    for nx in graph[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x]+1
            q.append(nx)

for _ in range(N-1):
    print((N-1-depth.pop())%2,end='')