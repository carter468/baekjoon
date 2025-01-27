# Jelly Raid
# Gold 3, BFS

from collections import deque

M = 120

r,c = map(int,input().split())
sx,sy,ex,ey = map(int,input().replace('(','').replace(')','').split())
sx,sy,ex,ey = sx-1,sy-1,ex-1,ey-1
grid = [input() for _ in range(r)]
p = int(input())
patrol = []
for _ in range(p):
    s = input()
    ss = s[2:].replace('(','').replace(')','').split()
    temp = []
    for i in range(int(s[0])):
        temp.append((int(ss[i*2])-1,int(ss[i*2+1])-1))
    patrol.append(temp+temp[-2:0:-1])

safe = [[[False]*c for _ in range(r)] for _ in range(M)]
for t in range(M):
    for i in range(r):
        for j in range(c):
            safe[t][i][j] = grid[i][j] == '.'

for t in range(M):
    for i in range(p):
        x,y = patrol[i][t%len(patrol[i])]
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny = x,y
            while 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '.':
                safe[t][nx][ny] = False
                nx += dx
                ny += dy

q = deque()
if safe[0][sx][sy]: q.append((0,sx,sy))
visited = [[[False]*c for _ in range(r)] for _ in range(M)]
while q:
    t,x,y = q.popleft()
    t += 1
    for nx,ny in (x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if (nx,ny) == (ex,ey): exit(print(t))
        if 0 <= nx < r and 0 <= ny < c and safe[t%120][nx][ny] and not visited[t%120][nx][ny]:
            visited[t%120][nx][ny] = True
            q.append((t,nx,ny))

print('IMPOSSIBLE')