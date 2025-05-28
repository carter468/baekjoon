# 인덕이와 산책
# Gold 2, BFS

from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N,M,T = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
C = tuple(map(int,input().split()))

visited = [INF]*(N+1)
visited[1] = 0
q = deque()
if C[0] != 1:
    q.append((1,0))
while q:
    x,t = q.popleft()
    if x == C[t%T]:
        q.append((x,t+1))
        continue
    for nx in graph[x]:
        if visited[nx] == INF:
            visited[nx] = t+1
            q.append((nx,t+1))

result = visited[N]
for i in range(1,N+1):
    t = visited[i]
    for j in range(t,t+T):
        if C[j%T] == i:
            break
    else: continue
    while True:
        if C[j%T] == N: break
        j += 1
    result = min(result,j)
print(result if result != INF else -1)