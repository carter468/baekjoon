# LCA
# Gold 3, LCA

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
parent[1] = 1
depth = [0]*(n+1)
q = [1]
while q:
    x = q.pop()
    for nx in graph[x]:
        if parent[nx] == 0:
            parent[nx] = x
            depth[nx] = depth[x]+1
            q.append(nx)

for _ in range(int(input())):
    a,b = map(int,input().split())
    if depth[a] < depth[b]: a,b = b,a
    while depth[a] != depth[b]:
        a = parent[a]
    while a != b:
        a,b = parent[a],parent[b]
    print(a)
