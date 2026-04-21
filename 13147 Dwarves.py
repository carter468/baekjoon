# Dwarves
# Gold 3, topological sorting

from collections import defaultdict,deque
import sys
input = sys.stdin.readline

graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(int(input())):
    a,b,c = input().split()
    if b == '>':
        a,c = c,a
    graph[a].append(c)
    indegree[c] += 1

q = deque()
for x in graph:
    if indegree[x] == 0:
        q.append(x)

c = len(indegree)
while q:
    x = q.popleft()
    c -= 1
    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

print('impossible' if c else 'possible')