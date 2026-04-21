# 안전한 건설 계획
# Gold 4, DFS

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1
visited = [False]*(N+1)
for i in range(1,N+1):
    if not visited[i]:
        visited[i] = True
        count += 1
        q = [i]
        while q:
            x = q.pop()
            for nx in graph[x]:
                if not visited[nx]:
                    visited[nx] = True
                    q.append(nx)
print(count)