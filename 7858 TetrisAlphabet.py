# Tetris Alphabet
# Gold 3, topological sorting

from collections import defaultdict
import heapq

N = int(input())
grid = [input() for _ in range(N)]

graph = defaultdict(set)
indegree = defaultdict(int)
arr = set(grid[-1])
for i in range(N-1):
    for j in range(20):
        a = grid[i][j]
        b = grid[i+1][j]
        arr.add(a)
        arr.add(b)
        if a != b and '.' not in (a,b) and a not in graph[b]:
            graph[b].add(a)
            indegree[a] += 1
arr.discard('.')

q = [a for a in arr if indegree[a] == 0]
heapq.heapify(q)
result = []
while q:
    x = heapq.heappop(q)
    result.append(x)
    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            heapq.heappush(q,nx)
print(''.join(result))