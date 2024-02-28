# 연구소 3
# Gold 3, bruteforcing, BFS

from collections import deque
import itertools
INF = 10**9

n,m = map(int,input().split())
arr = [tuple(input().split()) for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '2': virus.append((i,j))

result = INF
for c in itertools.combinations(range(len(virus)),m):
    visited = [[INF]*n for _ in range(n)]
    for i in c:
        x,y = virus[i]
        q = deque([(x,y)])
        visited[x][y] = 0
        while q:
            x,y = q.popleft()
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > visited[x][y]+1 and arr[nx][ny] != '1':
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
    t = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '0':
                t = max(t,visited[i][j])
    if t != INF: result = min(result,t)
print(result if result != INF else -1)