# 성곽
# Gold 3, DFS

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(M)]

visited = [[-1]*N for _ in range(M)]
idx = 0
count = []
for i in range(M):
    for j in range(N):
        if visited[i][j] == -1:
            q = [(i,j)]
            visited[i][j] = idx
            idx += 1
            c = 1
            while q:
                x,y = q.pop()
                for k,dx,dy in (0,0,-1),(1,-1,0),(2,0,1),(3,1,0):
                    nx,ny = x+dx,y+dy
                    if arr[x][y]>>k&1 == 0 and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[i][j]
                        q.append((nx,ny))
                        c += 1
            count.append(c)

result = 0
for x in range(M):
    for y in range(N):
        for k,dx,dy in (0,0,-1),(1,-1,0),(2,0,1),(3,1,0):
            nx,ny = x+dx,y+dy
            if nx < 0 or nx == M or ny < 0 or ny == N: continue
            a,b = visited[x][y],visited[nx][ny]
            if arr[x][y]>>k&1 and a != b:
                result = max(result,count[a]+count[b])

print(idx)
print(max(count))
print(result)