# 어떤 우유의 배달목록 (Easy)
# Gold 4, DFS

import sys
input = sys.stdin.readline

def dfs(x,end,dist):
    if x == end:
        count[x] += dist
        return True
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            if dfs(nx,end,dist+1):
                count[x] += dist
                return True
    return False

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = [0]*(N+1)
for _ in range(int(input())):
    query = tuple(map(int,input().split()))
    if query[0] == 2: print(count[query[1]])
    else:
        u,v = query[1],query[2]
        visited = [False]*(N+1)
        visited[u] = True
        dfs(u,v,0)