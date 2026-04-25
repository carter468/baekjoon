# Cow Contest
# Gold 4, DFS

def dfs(i,k):
    visited = [False]*(N+1)
    visited[i] = True
    q = [i]
    c = 0
    while q:
        x = q.pop()
        for nx in graph[k][x]:
            if not visited[nx]:
                c += 1
                visited[nx] = True
                q.append(nx)
    return c

N,M = map(int,input().split())
graph = [[[] for _ in range(N+1)] for _ in range(2)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[0][a].append(b)
    graph[1][b].append(a)

count = 0
for i in range(1,N+1):
    if dfs(i,0)+dfs(i,1) == N-1: count += 1
print(count)