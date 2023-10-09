# 적록색약
# Gold 5, DFS

def dfs():
    result = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                result += 1
                q = [(i,j)]
                visit[i][j] = 1
                while q:
                    x,y = q.pop()
                    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and grid[x][y] == grid[nx][ny]:
                            visit[nx][ny] = 1
                            q.append((nx,ny))
    return result

n = int(input())
grid = [list(input()) for _ in range(n)]

a = dfs()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'
b = dfs()

print(a,b)