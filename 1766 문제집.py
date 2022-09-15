# 문제집

import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]    # 그래프
indegree = [0]*(n+1)                # 진입차수
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []      # 힙
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)

ans = []
while q:
    x = heapq.heappop(q)
    ans.append(x)
    for i in graph[x]:
        indegree[i] -= 1    # 간선제거
        if indegree[i] == 0:
            heapq.heappush(q,i)

print(*ans)