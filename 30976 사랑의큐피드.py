# 사랑의 큐피드
# Platinum 4, bipartite matching

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
G = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
L = tuple(map(int,input().split()))
U = tuple(map(int,input().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if B[j] < L[i] and G[i] > U[j]:
            graph[i].append(j)

matching = [-1]*m

def dfs(node):
    if visited[node]: return False
    visited[node] = 1
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

for i in range(n):
    visited = [0]*n
    dfs(i)

print(m-matching.count(-1))