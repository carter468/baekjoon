# 연결 요소의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visit[node] = True
    for next in graph[node]:
        if not visit[next]:
            dfs(next)

visit = [False]*(n+1)
count = 0
for i in range(1,n+1):
    if not visit[i]:
        dfs(i)
        count += 1
print(count)