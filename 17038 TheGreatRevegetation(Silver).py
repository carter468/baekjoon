# The Great Revegetation (Silver)
# Gold 2, DFS

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = input().split()
    b,c = int(b),int(c)
    graph[b].append((c,a))
    graph[c].append((b,a))

visited = [0]*(N+1)
count = 0
for i in range(1,N+1):
    if visited[i] == 0:
        count += 1
        visited[i] = 1
        q = [i]
        while q:
            x = q.pop()
            for nx,c in graph[x]:
                if visited[nx] == 0:
                    if c == 'S': visited[nx] = visited[x]
                    else: visited[nx] = -visited[x]
                    q.append(nx)
                else:
                    if (c == 'S' and visited[nx] != visited[x]) or (c == 'D' and visited[nx] == visited[x]):
                        exit(print(0))

print('1'+'0'*count)