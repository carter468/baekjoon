# Stock Charts (Large)
# Platinum 2, bipartite matching

import sys
input = sys.stdin.readline

def dfs(node):
    if visited[node]: return False
    visited[node] = True
    for next in graph[node]:
        if matching[next] == -1:
            matching[next] = node
            return True
        else:
            prev = matching[next]
            if dfs(prev):
                matching[next] = node
                return True
    return False

for t in range(int(input())):
    N,K = map(int,input().split())
    arr = [tuple(map(int,input().split())) for _ in range(N)]

    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(K):
                if arr[i][k] <= arr[j][k]: break
            else:
                graph[i].append(j)
    
    matching = [-1]*N
    for i in range(N):
        visited = [False]*N
        dfs(i)

    print(f'Case #{t+1}: {matching.count(-1)}')