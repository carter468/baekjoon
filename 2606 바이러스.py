# 바이러스

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())   #컴퓨터 수
m = int(input())   #연결 수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)   # 방문 여부

def dfs(i):
    global cnt
    visited[i] = True
    for x in graph[i]:
        if visited[x] == False:
            cnt += 1
            dfs(x)
    
cnt = 0
dfs(1)
print(cnt)