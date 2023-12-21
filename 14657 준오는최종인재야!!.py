# 준오는 최종인재야!!
# Gold 2, DFS

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(idx,count,total):
    global result
    if count > result[0] or count == result[0] and total < result[2]:
        result = [count,idx,total]

    visited[idx] = True
    for node,cost in graph[idx]:
        if visited[node] == False:
            dfs(node,count+1,total+cost)

n,t = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

result = [0,0,0]

visited = [False]*(n+1)
dfs(1,1,0)
visited = [False]*(n+1)
dfs(result[1],1,0)

print((result[2]-1)//t+1)