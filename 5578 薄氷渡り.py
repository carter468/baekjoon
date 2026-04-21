# 薄氷渡り
# Gold 4, backtracking

def solve(x,y,c):
    global m
    m = max(m,c)

    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            solve(nx,ny,c+1)
            visited[nx][ny] = False

M = int(input())
N = int(input())
A = [tuple(map(int,input().split())) for _ in range(N)]

m = 0
for i in range(N):
    for j in range(M):
        if A[i][j] == 1:
            visited = [[False]*M for _ in range(N)]
            visited[i][j] = True
            solve(i,j,1)
print(m)