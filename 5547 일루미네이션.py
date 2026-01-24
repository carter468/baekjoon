# 일루미네이션
# Gold 4, DFS

W,H = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

visited = [[False]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            arr = []
            sur = True
            q = [(i,j)]
            while q:
                x,y = q.pop()
                arr.append((x,y))
                if x == 0 or y == 0 or x == H-1 or y == W-1: sur = False
                if x%2:
                    for nx,ny in (x-1,y-1),(x-1,y),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y):
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and A[nx][ny] == 0:
                            q.append((nx,ny))
                            visited[nx][ny] = True
                else:
                    for nx,ny in (x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y),(x+1,y+1):
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and A[nx][ny] == 0:
                            q.append((nx,ny))
                            visited[nx][ny] = True
            if sur:
                for x,y in arr:
                    A[x][y] = 1

result = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == 1:
            result += 6
            if i%2:
                for x,y in (i-1,j-1),(i-1,j),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j):
                    if 0 <= x < H and 0 <= y < W:
                        result -= A[x][y]
            else:
                for x,y in (i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j),(i+1,j+1):
                    if 0 <= x < H and 0 <= y < W:
                        result -= A[x][y]

print(result)