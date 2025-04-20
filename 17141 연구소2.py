# 연구소 2
# Gold 4, BFS, backtracking

from collections import deque
INF = 10**9

def dfs(idx):
    global result
    def bfs():
        q = deque()
        visited = [[-1]*N for _ in range(N)]

        for i in virus:
            x,y = cand[i] 
            q.append((x,y))
            visited[x][y] = 0

        while q:
            x,y = q.popleft()
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != '1' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
        
        for i in range(N):
            for j in range(N):
                if arr[i][j] != '1' and visited[i][j] == -1: return INF
        return visited[x][y]
    
    if len(virus) == M:
        result = min(result,bfs())
        return

    for i in range(idx,K):
        virus.append(i)
        dfs(i+1)
        virus.pop()

N,M = map(int,input().split())
arr = [input().split() for _ in range(N)]

cand = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '2': cand.append((i,j))
K = len(cand)

result = INF
virus = []
dfs(0)
print(result if result != INF else -1)