from collections import deque

def hash(a,b,c,d):
    return a*20**3+b*20**2+c*20+d

def check(a,b):
    if 0 <= a < n and 0 <= b < m: return 1
    else: return 0

n,m = map(int,input().split())
board = [input() for _ in range(n)]

coin = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coin.append((i,j))

q = deque([(*coin[0],*coin[1])])
visited = {hash(*q[0]):0}
while q:
    k = visited[hash(*q[0])]
    if k == 10: break
    x1,y1,x2,y2 = q.popleft()
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        a,b,c,d = x1+dx,y1+dy,x2+dx,y2+dy
        c1,c2 = check(a,b),check(c,d)
        if c1 and board[a][b] == '#': a,b = x1,y1
        if c2 and board[c][d] == '#': c,d = x2,y2
        if c1+c2 == 1:
            print(k+1)
            exit()
        h = hash(a,b,c,d)
        if (a,b) != (c,d) and c1 and c2 and h not in visited:
            visited[h] = k+1
            q.append((a,b,c,d))
print(-1)