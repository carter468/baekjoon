# 홍수
# Gold 5, DFS

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
H = tuple(map(int,input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    graph[u].append(v)
    graph[v].append(u)
input()

visited = [False]*N
q = []
for x in map(int,input().split()):
    q.append(x-1)
    visited[x-1] = True
while q:
    x = q.pop()
    for nx in graph[x]:
        if not visited[nx] and H[nx] > H[x]:
            visited[nx] = True
            q.append(nx)

print('no flood' if all(visited) else 'flood')