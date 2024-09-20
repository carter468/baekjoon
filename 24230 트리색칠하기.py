# 트리 색칠하기
# Gold 5, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global count
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            if color[nx-1] != color[x-1]:
                count += 1
            dfs(nx)
            
n = int(input())
color = tuple(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0 if color[0] == 0 else 1
visited = [False]*(n+1)
visited[1] = True
dfs(1)
print(count)
