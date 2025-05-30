# 영일 마을에 살고 있는 엄은 친구의 집에 가고 싶다
# Gold 5, DFS

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
graph = [[] for _ in range(N+2)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
gone = set(map(int,input().split()))

q = [1]
visited = [False]*(N+2)
visited[1] = True
count = 0
while q:
    x = q.pop()
    for nx in graph[x]:
        if not visited[nx] and nx not in gone:
            visited[nx] = True
            q.append(nx)
            count += 1
print(count)