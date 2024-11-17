# 트리의 루트를 찾아라
# Gold 3, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x):
    global flag,c
    if x in (a,b):
        flag = False
        return
    c += 1
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            DFS(nx)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
a,b,x = map(int,input().split())

if a == b == x:
    print(N)
    exit()
    
if a == x: a = b
elif b == x: b = a

count = 1
visited = [False]*(N+1)
visited[x] = True
for nx in graph[x]:
    visited[nx] = True
    flag = True
    c = 0
    DFS(nx)
    if flag: count += c
print(count)