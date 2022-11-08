# 너구리 구구

import sys
sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(now,dist):
    for next,d in graph[now]:
        if not visit[next]:
            visit[next] = True
            dfs(next,dist+d)
    distance.append(dist)

visit = [False]*(n+1)
visit[1] = True
distance = []
dfs(1,0)
print(max(distance))