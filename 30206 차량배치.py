# 차량 배치
# Gold 4, BFS, combinatorics

from collections import deque,defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visit = [0]*(n+1)
visit[1] = 1
dist = defaultdict(int)
while q:
    x = q.popleft()
    for nx in graph[x]:
        if visit[nx] == 0:
            visit[nx] = visit[x]+1
            dist[visit[nx]] += 1
            q.append(nx)

result = 2
for d in dist:
    result = result*(dist[d]+1)%(10**9+7)
print((result-1)%(10**9+7))