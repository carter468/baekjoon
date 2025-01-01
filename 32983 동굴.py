# 동굴
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

N,M,C = map(int,input().split())
x,y = map(int,input().split())
cave = [tuple(map(int,input().split())) for _ in range(N)]

x,y = x-1,y-1
dist = [[-1]*M for _ in range(N)]
dist[x][y] = 0
q = deque([(x,y)])
count = [0]*(N*M)
count[0] = cave[x][y]
while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M and cave[nx][ny] != -1 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y]+1
            q.append((nx,ny))
            count[dist[nx][ny]] += cave[nx][ny]
            
answer = 0
lupi = 0
for i in range(N*M):
    lupi += count[i]
    answer = max(answer,lupi-i*C)
print(answer)