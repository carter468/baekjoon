# 알고리즘 수업 - 깊이 우선 탐색 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# n,m,r = 5,5,1
# uv = [[1,4],[1,2],[2,3],[2,4],[3,4]]
n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]    # graph[i] : i와 연결된 노드번호
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)    
    graph[v].append(u)
         
visited = [0] * (n+1)       
def dfs(v):                   # 방문 노드, 방문 순서                
    global cnt
    visited[v] = cnt              # 방문 순서
    graph[v].sort()               
    graph[v].reverse()          # 내림차순 방문
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

cnt = 1
dfs(r)

for i in range(1,n+1):
    print(visited[i])