# 학부 연구생 민상
# Gold 5, implementation, DFS

import sys
input = sys.stdin.readline
D = (1,0),(0,-1),(-1,0),(0,1) # down, left, up, right

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

result = 0
visited = [[[False]*4 for _ in range(M)] for _ in range(N)]
check = [[False]*M for _ in range(N)]
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            for k in range(4):
                q.append((i,j,k))
            visited[i][j] = [True]*4

while q:
    x,y,d = q.pop()
    if not check[x][y]: 
        result += 1
        check[x][y] = True

    dx,dy = D[d]
    nx,ny = x+dx,y+dy

    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][d]:
        visited[nx][ny][d] = True
        if arr[nx][ny] == 1:
            if d%2 == 1: nd = 4-d
            else: nd = d
        elif arr[nx][ny] == 2:
            if d%2 == 0: nd = 2-d
            else: nd = d
        elif arr[nx][ny] == 3:
            if d%2 == 0: nd = (d+1)%4
            else: nd = (d-1)%4
        elif arr[nx][ny] == 4:
            if d%2 == 0: nd = (d-1)%4
            else: nd = (d+1)%4
        else: nd = d
        q.append((nx,ny,nd))

print(result)