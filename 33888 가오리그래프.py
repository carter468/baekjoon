# 가오리 그래프
# Gold 5, BFS

from collections import deque

N = int(input())

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(N+3):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    indegree[u] += 1
    indegree[v] += 1

for i in range(N+1):
    if indegree[i] == 1:
        f = i
        break

ce,abd = [],[]
q = deque([f])
visited = [False]*(N+1)
visited[f] = True
while q:
    x = q.popleft()
    if indegree[x] == 4: 
        ce.append(x)
    elif indegree[x] == 3:
        abd.append(x)
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            q.append(nx)

e,c = ce
b,d,a = abd

q = [b]
visited = [False]*(N+1)
visited[b] = True
while q:
    x = q.pop()
    if x in (a,d):
        if x == d:
            a,d = d,a
        break

    for nx in graph[x]:
        if not visited[nx] and x not in ce:
            visited[nx] = True
            q.append(nx)

if b > d: b,d = d,b

print(a,b,c,d,e,f)