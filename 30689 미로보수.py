# 미로 보수
# Gold 3, DFS

import sys
input = sys.stdin.readline

Move = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

n,m = map(int,input().split())
arr = [input() for _ in range(n)]
cost = [tuple(map(int,input().split())) for _ in range(n)]

k = 0
result = 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            k += 1
            visited[i][j] == k
            x,y = i,j
            while True:
                dx,dy = Move[arr[x][y]]
                nx,ny = x+dx,y+dy
                if nx < 0 or nx == n or ny < 0 or ny == m or 0 < visited[nx][ny] < k: break
                if visited[nx][ny] == k:
                    c = cost[x][y]
                    while (nx,ny) != (x,y):
                        c = min(c,cost[nx][ny])
                        dx,dy = Move[arr[nx][ny]]
                        nx,ny = nx+dx,ny+dy
                    result += c
                    break
                visited[nx][ny] = k
                x,y = nx,ny

print(result)