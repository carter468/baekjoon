# 양 구출 작전
# Gold 3, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    result = arr[x]
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            result += dfs(nx)
    return max(0,result)

n = int(input())
graph = [[] for _ in range(n+1)]
arr = [0]*(n+1)
for i in range(2,n+1):
    t,a,p = input().split()
    arr[i] = int(a)
    if t == 'W': arr[i] *= -1
    p = int(p)
    graph[i].append(p)
    graph[p].append(i)

visited = [False]*(n+1)
visited[1] = True
print(dfs(1))