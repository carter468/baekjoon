# Scoring Hack
# Gold 2, BFS

from collections import deque

N,A,B = map(int,input().split())

q = deque([(0,0,0)])
visited = [[False]*N for _ in range(N)]
visited[0][0] = True
while q:
    x,t,c = q.popleft()
    nt = t+1
    
    if x+A >= N or x+B >= N: exit(print(nt))

    for nx in (x+A,x+B):
        if not visited[nx][nt]:
            visited[nx][nt] = True
            q.append((nx,nt,c))
    
    nx = x*2
    if x == 0 or nx >= N+A or (c+1)*10 > nt: continue
    if nx >= N: exit(print(nt))
    if not visited[nx][nt]:
        visited[nx][nt] = True
        q.append((nx,nt,c+1))