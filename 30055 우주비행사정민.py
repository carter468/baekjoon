# 우주비행사 정민
# Platinum 5, BFS, implementation

from collections import deque
INF = 10**9

K,N1,M1,N2,M2 = map(int,input().split())
A,B = map(int,input().split())
R1,C1 = map(int,input().split())
R2,C2 = map(int,input().split())

hole = [[[INF]*M1 for _ in range(N1)],[[INF]*M2 for _ in range(N2)]]
q = deque()
for _ in range(K):
    d,dr,dc = map(int,input().split())
    hole[d-1][dr][dc] = 0
    q.append((0,d-1,dr,dc))
while q:
    c,d,x,y = q.popleft()
    if x%2 == 0:
        if d == 0:
            if y == M1-1: x += 1
            else: y += 1
        else:
            if y == M2-1: x += 1
            else: y += 1
    else:
        if d == 0:
            if y == 0: x = (x+1)%N1
            else: y -= 1
        else:
            if y == 0: x = (x+1)%N2
            else: y -= 1
    if hole[d][x][y] == INF:
        hole[d][x][y] = c+1
        q.append((c+1,d,x,y))

visited = [[[INF]*M1 for _ in range(N1)],[[INF]*M2 for _ in range(N2)]]
visited[0][0][0] = 0
q = deque([(0,0,0,0)])
temp = deque()
while q or temp:
    if not q:
        q.append(temp.popleft())
    while temp and q[0][0] == temp[0][0]:
        q.appendleft(temp.popleft())
        
    c,d,x,y = q.popleft()
    if (d,x,y) == (1,N2-1,M2-1):
        print(c)
        break

    if c != visited[d][x][y]: continue

    nc = c+1
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if d == 0 and 0 <= nx < N1 and 0 <= ny < M1 and nc < hole[d][nx][ny] and nc < visited[d][nx][ny]:
            visited[d][nx][ny] = nc
            q.append((nc,d,nx,ny))
        elif d == 1 and 0 <= nx < N2 and 0 <= ny < M2 and nc < hole[d][nx][ny] and nc < visited[d][nx][ny]:
            visited[d][nx][ny] = nc
            q.append((nc,d,nx,ny))

    nc = c+3
    if d == 0 and R1 <= x < R1+A and C1 <= y < C1+B:
        nx,ny = R2+x-R1,C2+y-C1
        if nc < hole[1][nx][ny] and nc < visited[1][nx][ny]:
            visited[1][nx][ny] = nc
            temp.append((nc,1,nx,ny))
    elif d == 1 and R2 <= x < R2+A and C2 <= y < C2+B:
        nx,ny = R1+x-R2,C1+y-C2
        if nc < hole[0][nx][ny] and nc < visited[0][nx][ny]:
            visited[0][nx][ny] = nc
            temp.append((nc,0,nx,ny))
else: print('hing...')