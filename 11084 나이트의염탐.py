# 나이트의 염탐
# Gold 2, BFS, DP

from collections import deque
MOD = 10**9+9

r,c = map(int,input().split())

dp = [[[-1,0] for _ in range(c)] for _ in range(r)]
dp[0][0] = [0,1]
q = deque([(0,0)])
while q:
    x,y = q.popleft()
    a,b = dp[x][y]
    for dx,dy in (1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1):
        nx,ny = x+dx,y+dy
        if 0 <= nx < r and 0 <= ny < c:
            if dp[nx][ny][0] == -1:
                dp[nx][ny] = [a+1,b]
                q.append((nx,ny))
            elif dp[nx][ny][0] == a+1:
                dp[nx][ny][1] = (dp[nx][ny][1]+b)%MOD

a,b = dp[-1][-1]
if a != -1: print(a,b)
else: print('None')