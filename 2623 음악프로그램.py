# 음악프로그램
# Gold 3, topological sorting

from collections import deque

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    arr = tuple(map(int,input().split()))
    for i in range(arr[0]-1):
        a,b = arr[i+1],arr[i+2]
        graph[a].append(b)
        indegree[b] += 1

q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
result = []
while q:
    x = q.popleft()
    result.append(x)
    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

if len(result) == N:
    print(*result,sep='\n')
else:
    print(0)