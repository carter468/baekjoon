# Piggy Back
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline

def BFS(idx,s,k):
    q = deque([s])
    dist[s][idx] = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx][idx] == -1:
                dist[nx][idx] = dist[x][idx]+k
                q.append(nx)

B,E,P,N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [[-1,-1,-1] for _ in range(N+1)]
BFS(0,1,B)
BFS(1,2,E)
BFS(2,N,P)

print(min([sum(dist[i]) for i in range(1,N+1)]))