# 레몬 경로
# Gold 1, BFS, modular multiplicative inverse

from collections import deque
import sys
input = sys.stdin.readline
MOD = 998244353

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,c = map(int,input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

result = [[0,0] for _ in range(N+1)]
q = deque([1])
visited = [[-1,0,0] for _ in range(N+1)]
visited[1] = [0,0,1]
while q:
    x = q.popleft()
    d,t,cnt = visited[x]
    for nx,c in graph[x]:
        if visited[nx][0] == -1:
            visited[nx] = [d+1,t+c*cnt,cnt]
            q.append(nx)
        elif visited[nx][0] == d+1:
            visited[nx][1] += t+c*cnt
            visited[nx][2] += cnt

for i in range(2,N+1):
    p,q = visited[i][1:]
    print(p*pow(q,MOD-2,MOD)%MOD)