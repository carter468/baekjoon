# 보스 몬스터 전리품
# Gold 3, 너비 우선 탐색

import sys
input = sys.stdin.readline
from collections import deque

n,m,p = map(int,input().split())
mmworld = []    # 멤멤월드
meet = []       # 보스와 만난 유저
visit = [[False for _ in range(m)] for _ in range(n)]   # 방문체크
dps = {}    # 유저별 dps

for i in range(n):
    mmworld.append(input().strip())
    for j in range(m):
        if mmworld[i][j] == 'B':
            q = deque([(i,j)])    # 보스 위치
            visit[i][j] = True
for _ in range(p):
    u,d = input().split()
    dps[u] = int(d)
boss_hp = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
while boss_hp>0:
    for _ in range(len(q)):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and mmworld[nx][ny] != 'X':    # 이동가능
                visit[nx][ny] = True
                q.append((nx,ny))
                if mmworld[nx][ny] != '.':  # 유저 조우
                    meet.append(mmworld[nx][ny])
    for i in meet:
        boss_hp -= dps[i]
                
print(len(meet))