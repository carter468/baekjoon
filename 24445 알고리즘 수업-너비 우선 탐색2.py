# 알고리즘 수업-너비 우선 탐색 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]    # graph[i] : i와 연결된 노드번호
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)    
    graph[v].append(u)

visited = [0] * (n+1)
q = []          # queue
def bfs(v):
    global cnt
    for i in range(1,n+1):
        if i != v:
            visited[i] = 0
    visited[v] = cnt
    cnt += 1
    q.append(v)
    while q:
        u = q.pop(0)
        graph[u].sort()
        graph[u].reverse()
        for i in graph[u]:
            if visited[i] == 0:
                visited[i] = cnt
                cnt += 1
                q.append(i)

cnt = 1
bfs(r)

for i in range(1,n+1):
    print(visited[i])