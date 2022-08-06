# 트리의 지름

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(i):
    for x in graph[i]:
        if visited[x[0]] == -1 or visited[i] + x[1] < visited[x[0]]:
            visited[x[0]] = visited[i] + x[1]
            dfs(x[0])

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

visited = [-1]*(v+1)
visited[1] = 0
dfs(1)

temp = visited.index(max(visited))
visited = [-1]*(v+1)
visited[temp] = 0
dfs(temp)
print(max(visited))