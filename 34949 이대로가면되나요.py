# 이대로 가면 되나요?
# Gold 5, BFS

from collections import deque

N = int(input())
A = tuple(map(int,input().split()))

graph = [[] for _ in range(N+1)]
for i,a in enumerate(A):
    graph[a].append(i+1)

result = [-1]*N+[0]
q = deque([N])
while q:
    x = q.popleft()
    for nx in graph[x]:
        if result[nx] == -1:
            result[nx] = result[x]+1
            q.append(nx)

print(*result[1:],sep='\n')