# 로봇 청소기
# Gold 5, implementation, simulation

D = [(-1,0),(0,1),(1,0),(0,-1)]

n,m = map(int,input().split())
x,y,d = map(int,input().split())
arr = [input().split() for _ in range(n)]

count = 0
visited = [[False]*m for _ in range(n)]
while True:
    if not visited[x][y]:
        visited[x][y] = True
        count += 1
    for i in range(4):
        nd = (d-1-i)%4
        nx,ny = x+D[nd][0],y+D[nd][1]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '0' and not visited[nx][ny]:
            x,y,d = nx,ny,nd
            break
    else:
        x -= D[d][0]
        y -= D[d][1]
        if x < 0 or x == n or y < 0 or y == m or arr[x][y] == '1':
            break
        
print(count)
