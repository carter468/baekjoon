# 두 로봇
# Gold 4, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y,z):
    if x == e:
        print(y-z)
        exit()
    
    for nx,c in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx,y+c,max(z,c))

n,s,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visited = [False]*(n+1)
visited[s] = True
dfs(s,0,0)
