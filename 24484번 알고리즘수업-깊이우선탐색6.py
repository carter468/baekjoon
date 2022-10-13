# 알고리즘수업-깊이우선탐색6

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node,depth):
    global answer,count
    answer += depth*count
    count += 1
    visit[node] = True
    graph[node].sort(reverse=True)
    for next in graph[node]:
        if not visit[next]:
            dfs(next,depth+1)
answer,count = 0,1
dfs(r,0)
print(answer)