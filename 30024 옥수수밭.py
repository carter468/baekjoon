# 옥수수밭
# Gold 4, priority queue

import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
corn = [tuple(map(int,input().split())) for _ in range(n)]

visit = [[0]*m for _ in range(n)]
q = []
for i in range(n):
    for j in range(m):
        if i in (0,n-1) or j in (0,m-1):
            visit[i][j] = 1
            heapq.heappush(q,(-corn[i][j],i,j))

for _ in range(int(input())):
    x = heapq.heappop(q)
    print(x[1]+1,x[2]+1)
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        nx,ny = x[1]+dx,x[2]+dy
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = 1
            heapq.heappush(q,(-corn[nx][ny],nx,ny))