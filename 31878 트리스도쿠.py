# 트리 스도쿠
# Gold 2, BFS, constructive

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = sorted([(a,i) for i,a in enumerate(map(int,input().split()),1)])
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
result = [None]*(N+1)
while q:
    x = q.popleft()
    result[x] = A.pop()[1]
    for nx in graph[x]:
        if result[nx] == None:
            q.append(nx)

print('YES')
print(*result[1:])