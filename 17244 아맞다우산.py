# 아맞다우산
# Gold 2, BFS, bitmask

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    visit = [[-1]*n for _ in range(m)]
    visit[x][y] = 0
    q = deque([(x,y)])
    t = 0
    result = [0]*(c+2)
    while t != c+1:
        x,y = q.popleft()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == -1 and grid[nx][ny] != '#':
                if grid[nx][ny] == 'X':
                    for i in range(c):
                        if (nx,ny) == p[i]:
                            result[i] = visit[x][y]+1
                            break
                    t += 1
                elif grid[nx][ny] == 'S':
                    result[-2] = visit[x][y]+1
                    t += 1
                elif grid[nx][ny] == 'E':
                    result[-1] = visit[x][y]+1
                    t += 1
                visit[nx][ny] = visit[x][y]+1
                q.append((nx,ny))
    return result

def dfs(k,r,l):
    global answer
    if k == 2**c-1:
        answer = min(answer,r+dist[l][-1])
        return
    for i in range(c):
        if k&(1<<i) == 0:
            dfs(k|(1<<i),r+dist[l][i],i)

n,m = map(int,input().split())
grid = [input().strip() for _ in range(m)]

p = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S': s = (i,j)
        if grid[i][j] == 'X': p.append((i,j))
c = len(p)

dist = [bfs(*p[i]) for i in range(c)]

answer = 10**9
for i in range(c):
    dfs(1<<i,dist[i][-2],i)

print(answer if answer != 10**9 else bfs(*s)[-1])