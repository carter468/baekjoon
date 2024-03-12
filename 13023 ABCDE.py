# ABCDE
# Gold 5, DFS, backtracking

import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

def dfs(i,c):
    if c == 5:
        print(1)
        exit()
    for ni in graph[i]:
        if not visited[ni]:
            visited[ni] = True
            dfs(ni,c+1)
            visited[ni] = False

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited = [False]*n
    visited[i] = True
    dfs(i,1)
print(0)