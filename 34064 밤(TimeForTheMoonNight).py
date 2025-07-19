# 밤(Time For The Moon Night)
# Gold 4, DFS, combinatorics

N,M,K = map(int,input().split())
star = [[False]*(M+1) for _ in range(N+1)]
for _ in range(K):
    x,y = map(int,input().split())
    star[x][y] = True
a1,b1,a2,b2,a3,b3,a4,b4 = *map(int,input().split()),*map(int,input().split()),*map(int,input().split()),*map(int,input().split())

visited = [[-1]*(M+1) for _ in range(N+1)]
c = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if star[i][j] == False and visited[i][j] == -1:
            visited[i][j] = c
            q = [(i,j)]
            while q:
                x,y = q.pop()
                for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0 < nx <= N and 0 < ny <= M and star[nx][ny] == False and visited[nx][ny] == -1:
                        visited[nx][ny] = c
                        q.append((nx,ny))
            c += 1

count = [0]*c
for i in range(a1,a2+1):
    for j in range(b1,b2+1):
        if star[i][j] == False:
            count[visited[i][j]] += 1

result = 0
for i in range(a3,a4+1):
    for j in range(b3,b4+1):
        if star[i][j] == False:
            result += count[visited[i][j]]
print(result)