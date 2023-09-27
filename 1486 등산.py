# 등산
# Gold 2, dijkstra

from heapq import heappush,heappop

INF = 10**9

N,M,T,D = map(int,input().split())
arr = [input() for _ in range(N)]

grid = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        a = ord(arr[i][j])
        if a >= 97: grid[i][j] = a-71
        else: grid[i][j] = a-65

dist1 = [[INF]*M for _ in range(N)]
q = [(0,0,0)]
dist1[0][0] = 0
while q:
    d,x,y = heappop(q)
    if d > dist1[x][y]: continue
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M:
            k = grid[nx][ny]-grid[x][y]
            if abs(k) <= T:
                if k > 0:
                    nd = d+k*k
                else:
                    nd = d+1
                if nd < dist1[nx][ny]:
                    dist1[nx][ny] = nd
                    heappush(q,(nd,nx,ny))

dist2 = [[INF]*M for _ in range(N)]
q = [(0,0,0)]             
dist2[0][0] = 0
while q:
    d,x,y = heappop(q)
    if d > dist2[x][y]: continue
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M:
            k = grid[x][y]-grid[nx][ny]
            if abs(k) <= T:
                if k > 0:
                    nd = d+k*k
                else:
                    nd = d+1
                if nd < dist2[nx][ny]:
                    dist2[nx][ny] = nd
                    heappush(q,(nd,nx,ny))

result = 0
for i in range(N):
    for j in range(M):
        if dist1[i][j]+dist2[i][j] <= D:
            result = max(result,grid[i][j])
print(result)