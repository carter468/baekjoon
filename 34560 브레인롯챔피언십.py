# 브레인롯 챔피언십
# Gold 2, topological sorting

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
character = []
for _ in range(N):
    name,p,a,s = input().split()
    character.append((int(p),int(a),int(s),name))

indegree = [0]*N
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        c = 0
        for k in range(3):
            if character[i][k] > character[j][k]: c += 1
            elif character[i][k] < character[j][k]: c -= 1
        if c > 0:
            graph[i].append(j)
            indegree[j] += 1
        elif c < 0:
            graph[j].append(i)
            indegree[i] += 1

result = []
q = deque()
for i in range(N):
    if indegree[i] == 0:
        q.append(i)
        result.append(character[i][3])

count = 0
while q:
    x = q.popleft()
    count += 1
    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

if count == N:
    print(*sorted(result),sep='\n')
else:
    print('Paradoxe Absurdo')