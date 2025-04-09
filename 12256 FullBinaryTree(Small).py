# Full Binary Tree (Small)
# Gold 3, DFS, tree DP

import sys
input = sys.stdin.readline

def dfs(x):
    arr = []
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            arr.append(dfs(nx))
    if len(arr) >= 2: return sum(sorted(arr)[-2:])+1
    else: return 1

for t in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    result = N
    for i in range(1,N+1):
        visited = [False]*(N+1)
        visited[i] = True
        result = min(result,N-dfs(i))
    
    print(f'Case #{t+1}: {result}')