# 윤이는 엄청난 것을 훔쳐갔습니다
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    s = int(s)
    visited = [-1]*(N+1)
    visited[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x]+1
                q.append(nx)
    return visited

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    indegree[u] += 1
    indegree[v] += 1
va,vb,vc = map(bfs,input().split())

for i in range(1,N+1):
    if indegree[i] == 1 and va[i] < min(vb[i],vc[i]):
        print('YES')
        break
else:
    print('NO')