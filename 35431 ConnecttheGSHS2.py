# Connect the GSHS 2
# Gold 3, greedy, BFS

from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
d = [10**9]*K
result = 10**9
for k in range(K):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)
    
    for i in range(1,N+1):
        m = 0
        q = deque([i])
        visited = [-1]*(N+1)
        visited[i] = 0
        while q:
            u = q.popleft()
            m = max(m,visited[u])
            for v in graph[u]:
                if visited[v] == -1:
                    visited[v] = visited[u]+1
                    q.append(v)
        d[k] = min(d[k],m)

d.sort()
m = d.pop()
c = 2
while d:
    a = d.pop()
    m = max(m,a+c//2)
    c += 1
print(m)