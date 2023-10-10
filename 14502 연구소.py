# 연구소
# Gold 4, bruteforcing

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

empty = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            empty.append((i,j))

result = 0
l = len(empty)
for a in range(l):
    for b in range(a+1,l):
        for c in range(b+1,l):
            grid[empty[a][0]][empty[a][1]] = 1
            grid[empty[b][0]][empty[b][1]] = 1
            grid[empty[c][0]][empty[c][1]] = 1

            visit = [[False]*m for _ in range(n)]
            count = l-3
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 2:
                        q = [(i,j)]
                        while q:
                            x,y = q.pop()
                            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and grid[nx][ny] == 0:
                                    count -= 1
                                    q.append((nx,ny))
                                    visit[nx][ny] = True
            result = max(result,count)

            grid[empty[a][0]][empty[a][1]] = 0
            grid[empty[b][0]][empty[b][1]] = 0
            grid[empty[c][0]][empty[c][1]] = 0

print(result)