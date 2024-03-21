# 인구 이동
# Gold 4, DFS

n,l,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

count = 0
while True:
    idx = 0
    visited = [[-1]*n for _ in range(n)]
    p = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                visited[i][j] = idx
                p.append(arr[i][j])
                c = 1
                q = [(i,j)]
                while q:
                    x,y = q.pop()
                    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and l <= abs(arr[x][y]-arr[nx][ny]) <= r:
                            visited[nx][ny] = idx
                            p[-1] += arr[nx][ny]
                            q.append((nx,ny))
                            c += 1
                p[-1] //= c
                idx += 1
    flag = False
    for x in range(n):
        for y in range(n):
            if arr[x][y] != p[visited[x][y]]:
                arr[x][y] = p[visited[x][y]]
                flag = True
    if not flag: break
    count += 1
print(count)